from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'  # Modificamos el modelo de órdenes de venta

    @api.model
    def create_invoice_auto(self):
        """Esta función generará automáticamente la factura para el pedido confirmado."""
        for order in self:
            if order.state == 'sale':  # Verifica si el pedido está confirmado
                order.action_invoice_create()  # Crea la factura automáticamente
