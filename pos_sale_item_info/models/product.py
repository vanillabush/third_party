# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Product(models.Model):
    _inherit = 'product.product'

    show_qty_in_pos = fields.Boolean(
        string="Show Available Qty in POS?",
        copy=False,
    )

    @api.onchange('type')
    def _onchange_type_pos(self):
        for rec in self:
            if rec.type != 'service':
                rec.show_qty_in_pos = False

    def _load_pos_data_fields(self, config_id):
        res = super()._load_pos_data_fields(config_id);
        res.extend(['qty_available','show_qty_in_pos'])
        return res