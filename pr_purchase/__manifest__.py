# -*- coding: utf-8 -*-
{
    'name': "Advanced Enterprise Purchase",
    'summary': """
        This Module is created to manage Purchase""",

    'description': """
        
    """,

    'author': "Mahmoud Salah",
    'company': "Advanced Enterprise",
    'website': "https://webmail.Advanced Enterprise.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Purchase/Purchase',
    'version': '17.0.1.0.0',
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    'depends': ['purchase', 'pr_base'],

    # always loaded
    'data': [
        'report/custom_purchase_header_footer.xml',
        'report/custom_purchase_order_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'assets': {
    }
}
