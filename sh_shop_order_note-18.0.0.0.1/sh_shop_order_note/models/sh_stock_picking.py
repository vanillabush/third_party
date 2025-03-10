# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sh_order_comment_picking = fields.Text(
        string="Customer Order Comment",
        translate=True
    )

    @api.model_create_multi
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        sale_order = self.env['sale.order'].sudo().search(
            [('name', '=', res.origin)])
        res.update({
            'sh_order_comment_picking': sale_order.sh_order_comment,
        })
        return res
