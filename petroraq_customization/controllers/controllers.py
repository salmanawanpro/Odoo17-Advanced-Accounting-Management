# -*- coding: utf-8 -*-
# from odoo import http


# class Advanced EnterpriseCustomization(http.Controller):
#     @http.route('/Advanced Enterprise_customization/Advanced Enterprise_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/Advanced Enterprise_customization/Advanced Enterprise_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('Advanced Enterprise_customization.listing', {
#             'root': '/Advanced Enterprise_customization/Advanced Enterprise_customization',
#             'objects': http.request.env['Advanced Enterprise_customization.Advanced Enterprise_customization'].search([]),
#         })

#     @http.route('/Advanced Enterprise_customization/Advanced Enterprise_customization/objects/<model("Advanced Enterprise_customization.Advanced Enterprise_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('Advanced Enterprise_customization.object', {
#             'object': obj
#         })

