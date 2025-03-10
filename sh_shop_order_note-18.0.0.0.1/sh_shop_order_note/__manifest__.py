# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Customer Note in Website Cart/Order",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "website",
    "summary": "Customer Note In Website Cart Odoo, Customer Note In Website Order, Manage Client Notes, Customer Comments Module,Invoice User Note ,Delivery Order Customer Note,Manage Notes Customer Note in Website Cart/Order Customer Note in Website Cart Module Customer Notes in Online Orders Order Note Module for Website Customer Comments in Cart/Order Website Cart Customer Message Tool Customer Note Integration in E-commerce Cart/Order Customer Note Functionality Add Notes to Online Orders Customer Note Field in Website Cart Website Order Customer Note Customer Note in Checkout Customer Note in invoice Cart Customer Note Functionality Customer Note on Order Page Odoo",
    "description": """
Sometime customer comments on product is very important for improving product quality, service, his satisfy their needs, and eventually to keep them loyal to your brand on product. You will provide this feature using 'Customer Note in Website Cart/Order' module. you can manage customer comment on each order,order report, invoice, invoice report, delivery, delivery report, so you can easily interact with customer.
 Customer Note In Website Cart Odoo, Customer Note In Website Order Odoo
 Manage Customer Comments Module, Handle User Comment On Invoice, Invoice Report, Provide Controlling On Customer Delivery, Delivery Report, Order And Order Report Odoo.
 Manage Customer Comments Module, Handle Comments Of User In, Invoice, Invoice Report, Delivery, Delivery Report, Order And Order Report Odoo """,
    "version": "0.0.1",
    "depends": [
        "sale_management",
        "stock",
        "account",
        "website_sale",
    ],
    "application": True,
    "data": [
        "views/sh_sale_order_view.xml",
        "views/sh_stock_picking_view.xml",
        "views/sh_account_invoice_view.xml",
        "report/report_sh_sale_order.xml",
        "report/report_sh_account_invoice.xml",
        "report/report_sh_delivery_slip.xml",
        "report/report_sh_stock_picking_operation.xml",
        "views/sh_website_sale_template.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'sh_shop_order_note/static/src/js/custom.js',
        ],
    },
    "images": [
        "static/description/background.png",
    ],
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 20,
    "currency": "EUR"
}
