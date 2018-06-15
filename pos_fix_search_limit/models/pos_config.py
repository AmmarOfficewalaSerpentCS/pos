# Copyright 2004-2010 OpenERP SA
# Copyright 2017 RGB Consulting S.L. (https://www.rgbconsulting.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    search_limit = fields.Integer(string='Search Lmit',
                                  default=100,
                                  help="number of products will diaplay based "
                                       "on this number.")
