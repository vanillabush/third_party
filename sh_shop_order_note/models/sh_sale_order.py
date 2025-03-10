# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sh_order_comment = fields.Char(
        string="Customer Order Comment",
        translate=True
    )

    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'sh_customer_order_comment_id': self.sh_order_comment,
        })
        return res
