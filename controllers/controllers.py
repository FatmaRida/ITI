# -*- coding: utf-8 -*-
# from odoo import http


# class Nasrcity(http.Controller):
#     @http.route('/nasrcity/nasrcity/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nasrcity/nasrcity/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nasrcity.listing', {
#             'root': '/nasrcity/nasrcity',
#             'objects': http.request.env['nasrcity.nasrcity'].search([]),
#         })

#     @http.route('/nasrcity/nasrcity/objects/<model("nasrcity.nasrcity"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nasrcity.object', {
#             'object': obj
#         })
