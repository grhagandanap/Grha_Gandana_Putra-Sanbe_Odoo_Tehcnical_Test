# -*- coding: utf-8 -*-
# from odoo import http


# class PharmacyLogistics(http.Controller):
#     @http.route('/pharmacy_logistics/pharmacy_logistics', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pharmacy_logistics/pharmacy_logistics/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pharmacy_logistics.listing', {
#             'root': '/pharmacy_logistics/pharmacy_logistics',
#             'objects': http.request.env['pharmacy_logistics.pharmacy_logistics'].search([]),
#         })

#     @http.route('/pharmacy_logistics/pharmacy_logistics/objects/<model("pharmacy_logistics.pharmacy_logistics"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pharmacy_logistics.object', {
#             'object': obj
#         })
