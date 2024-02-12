# -*- coding: utf-8 -*-
# from odoo import http


# class MtxWebSite(http.Controller):
#     @http.route('/mtx_web_site/mtx_web_site', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mtx_web_site/mtx_web_site/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mtx_web_site.listing', {
#             'root': '/mtx_web_site/mtx_web_site',
#             'objects': http.request.env['mtx_web_site.mtx_web_site'].search([]),
#         })

#     @http.route('/mtx_web_site/mtx_web_site/objects/<model("mtx_web_site.mtx_web_site"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mtx_web_site.object', {
#             'object': obj
#         })