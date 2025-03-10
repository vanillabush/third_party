/** @odoo-module */

import { Component } from "@odoo/owl";
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";


export class CustomProductQty extends ProductCard {
    static template = "point_of_sale.ProductCard";
    
    static props = {
        ...ProductCard.props,
        productQtyAvailable: { Number, optional: true },
        uomId: { String, optional: true}
    };

    static defaultProps = {
        ...ProductCard.defaultProps,
        productQtyAvailable: "",
        uomId: "",
    };
};


//odoo.define('pos_sale_item_info.point_of_sale', function (require) {
//"use strict";

//var models = require('point_of_sale.models');
////var _super_posmodel = models.PosModel.prototype;

////models.PosModel = models.PosModel.extend({
////    initialize: function(session, attributes) {
////        var product_model = _.find(this.models, function (model) {
////            return model.model === "product.product";
////        });
////        product_model.fields.push('qty_available');
////        product_model.fields.push('type');
////        product_model.fields.push('show_qty_in_pos');
////        return _super_posmodel.initialize.call(this,session,attributes);
////    },
////})
//models.load_fields('product.product', ['qty_available', 'type', 'show_qty_in_pos']);

//});

