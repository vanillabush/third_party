/** @odoo-module **/

import PaymentForm from '@payment/js/payment_form';
import { rpc } from "@web/core/network/rpc";


PaymentForm.include({
    events: Object.assign({}, PaymentForm.prototype.events || {}, {
        'click [name="o_payment_submit_button"]': '_submitForm',
    }),

    async _submitForm(ev) {
        
        await this._super(...arguments);

        var sh_customer_order_comment = $("#sh_customer_order_comment_id").val();
        
        rpc("/shop/sh_customer_order_comment",{
            comment: sh_customer_order_comment,
        })

        
    },
});
