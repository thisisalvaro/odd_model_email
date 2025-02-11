from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def send_order_email(self):
        """Envía un correo electrónico cuando se confirma un pedido."""
        for order in self:
            if order.state == 'sale':  # Solo cuando el pedido está confirmado
                template = self.env.ref('auto_email_order.email_template_order_confirmed')
                template.send_mail(order.id, force_send=True)  # Enviar el correo automáticamente
