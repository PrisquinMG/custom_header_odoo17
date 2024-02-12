# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class HomePage(http.Controller):
    @http.route('/mtx_web_site', auth='public', website=True)
    def index(self, **kw):
        return request.render('mtx_web_site.home_page', {})