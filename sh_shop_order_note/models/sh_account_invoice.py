# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    sh_order_comment_invoice = fields.Text(
        string="Customer Order Comment",
        translate=True
    )
