# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'academy.sale.wizard'
    _description = 'Testing v14 wizard'
    
    def _default_session(self):
        return self.env['academy.session'].browse(self._context.get('active_id'))
    
    session_id = fields.Many2one(comodel_name='academy.session',
                                 string='Session',
                                 required=True,
                                 default=_default_session)

    
    def create_sale_orders(self):

        order_id = self.env['sale.order'].create({
            'partner_id': 5,
            'session_id': self.session_id.id,
            'order_line': [(0, 0, {'product_id': 14, 'price_unit': 100.0})]
        })