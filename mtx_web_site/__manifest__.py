# -*- coding: utf-8 -*-
{
    'name': "mtx_web_site",

    'summary': """Site web MTechniix""",

    'author': "Mtechniix",
    'website': "https://www.metchniix.com",
    
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'views/templates.xml',
        'views/home_page.xml',

        'views/templates/pages/services/erp_odoo.xml',
        # 'templates/layouts/header.xml',

        #'views/assets.xml',
    ],
    
}
