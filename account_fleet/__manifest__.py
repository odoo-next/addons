# -*- coding: utf-8 -*-
{
    'name': "Account Fleet",

    'summary': """
        Link Invoices with Fleet""",

    'description': """
        Add vehicles and drivers assignation on Invoices. These Statistics can also be accessed directly from the vehicle view.
    """,

    'author': "BADEP",
    'website': "https://badep.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '13.0.2.0',

    # any module necessary for this one to work correctly
    'depends': ['account', 'fleet'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_view.xml',
        'views/fleet_view.xml',
    ],
    'installable': True,
    'price': 49.00,
    'currency': 'USD',
}