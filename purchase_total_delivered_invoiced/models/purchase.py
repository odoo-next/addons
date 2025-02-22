# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    amount_received = fields.Monetary(string=u'Total Delivered', store=True, readonly=True, compute='_amount_received_invoiced')
    amount_invoiced = fields.Monetary(string=u'Total Invoiced', store=True, readonly=True, compute='_amount_received_invoiced')
    
    @api.depends('order_line.price_received', 'order_line.price_invoiced')
    def _amount_received_invoiced(self):
        for order in self:
            order.update({
                'amount_received': sum(order.order_line.mapped('price_received')),
                'amount_invoiced': sum(order.order_line.mapped('price_invoiced')),
            })

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    price_received = fields.Monetary(compute='_compute_amount_received_invoiced', string='Amount Delivered', readonly=True, store=True)
    price_invoiced = fields.Monetary(compute='_compute_amount_received_invoiced', string='Amount Invoiced', readonly=True, store=True)

    @api.depends('price_total', 'qty_received', 'qty_invoiced')
    def _compute_amount_received_invoiced(self):
        for line in self:
            line.update({
                'price_received': line.price_total * (line.qty_received / line.product_qty) if line.product_qty else 0,
                'price_invoiced': line.price_total * (line.qty_invoiced / line.product_qty) if line.product_qty else 0,
            })


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    price_received = fields.Float('Total livré', readonly=True)
    price_invoiced = fields.Float('Total facturé', readonly=True)

    def _select(self):
        return super()._select() + ", sum(l.qty_received / line_uom.factor * product_uom.factor) as qty_received, sum(l.qty_invoiced / line_uom.factor * product_uom.factor) as qty_billed"
