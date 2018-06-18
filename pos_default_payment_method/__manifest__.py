# Copyright (C) 2017-TODAY Camptocamp SA (<http://www.camptocamp.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'POS Default payment mehotd',
    'version': '11.0.1.0.0',
    'author': 'Camptocamp, '
              'Serpent Consulting Services PVT.LTD, '
              'Odoo Community Association (OCA)',
    'category': 'Sales Management',
    'depends': [
        'point_of_sale',
    ],
    'demo': [],
    'website': 'https://github.com/OCA/pos',
    'data': [
        'views/assets.xml',
        'views/pos_config_view.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
