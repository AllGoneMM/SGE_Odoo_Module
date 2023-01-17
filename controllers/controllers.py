# -*- coding: utf-8 -*-
# from odoo import http


# class SgeModule(http.Controller):
#     @http.route('/sge_module/sge_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sge_module/sge_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sge_module.listing', {
#             'root': '/sge_module/sge_module',
#             'objects': http.request.env['sge_module.sge_module'].search([]),
#         })

#     @http.route('/sge_module/sge_module/objects/<model("sge_module.sge_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sge_module.object', {
#             'object': obj
#         })
