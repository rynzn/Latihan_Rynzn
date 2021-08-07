# -*- coding: utf-8 -*-
# from odoo import http


# class LatihanRynzn(http.Controller):
#     @http.route('/latihan_rynzn/latihan_rynzn/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan_rynzn/latihan_rynzn/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('latihan_rynzn.listing', {
#             'root': '/latihan_rynzn/latihan_rynzn',
#             'objects': http.request.env['latihan_rynzn.latihan_rynzn'].search([]),
#         })

#     @http.route('/latihan_rynzn/latihan_rynzn/objects/<model("latihan_rynzn.latihan_rynzn"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('latihan_rynzn.object', {
#             'object': obj
#         })
