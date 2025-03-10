# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import http, SUPERUSER_ID
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleCustom(WebsiteSale):

    @http.route(['/shop/sh_customer_order_comment'], type='json', auth="public", methods=['POST'], website=True)
    def sh_customer_order_comment(self, **post):
        # print(f'\n\n\n>>> 13 | {post}:  ')
        
        if post.get('comment'):
            order = request.website.with_user(SUPERUSER_ID).sale_get_order()
            # print(f'\n\n\n>>> 17 | {order}:  ')
            # redirection = self.checkout_redirection(order)
            # print(f'\n\n\n>>> 19 | {redirection}:  ')
            # if redirection:
            #     return redirection

            if order and order.id:
                # print(f'\n\n\n>>> 24  in if| {order}:  ')
                order.with_user(SUPERUSER_ID).write({'sh_order_comment': post.get('comment')})
        
        return True
