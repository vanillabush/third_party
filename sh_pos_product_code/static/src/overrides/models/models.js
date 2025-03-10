/** @odoo-module **/

import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";

import { patch } from "@web/core/utils/patch";

patch(PosOrderline.prototype, {
  getDisplayData() {
    var res = super.getDisplayData(...arguments);
    if (this.get_product() && this.get_product().default_code) {      
      res["product_default_code_in_cart"] =
        !this.order_id.finalized && this.config.sh_enable_product_code_in_cart
          ? this.get_product().default_code
          : false;
      res["product_default_code_in_receipt"] =
        this.order_id.finalized &&
        this.config.sh_enable_product_code_in_receipt
          ? this.get_product().default_code
          : false;
    }
    return res;
  },
});
