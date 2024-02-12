from odoo import http
from odoo.http import request


class HomePage(http.Controller):
    @http.route('/mtx_web_site/nos-services/erp-odoo', auth='public', website=True)
    def index(self, **kw):
        return request.render('mtx_web_site.erp_odoo_page', {})