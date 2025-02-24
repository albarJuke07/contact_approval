# -*- coding: utf-8 -*-
{
    'name': "contact_approval",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'purchase'],

    # always loaded
    'data': [
        'security/res_group.xml',
        'security/ir.model.access.csv',
        'views/res_partner_form_view_inherit.xml',
        'views/sale_order_form_view_inherit.xml',
        'views/purchase_order_form_view_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

