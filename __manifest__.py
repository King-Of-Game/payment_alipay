# -*- coding: utf-8 -*-
{
    'name': "支付宝",

    'summary': """支付宝集成支付""",

    'description': """
        支付宝集成支付
    """,
    'author': "King-Of-Game",
    'website': "https://github.com/King-Of-Game/payment_alipay",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['payment'],

    # always loaded
    'data': [
        'security/data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    # other parameter
    "application": True,
    'installable': True,
    'license': 'LGPL-3',
}
