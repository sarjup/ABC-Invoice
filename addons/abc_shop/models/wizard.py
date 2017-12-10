from odoo import api, fields, models

class SaleInvoice(models.TransientModel):
    _name = 'abc.sale.wizard'
    _description = 'Product sale Wizard'
    
    number = fields.Char(string='Bill No.')
    product_ids = fields.Many2many('abc.products', string = 'Product')
    date_invoice = fields.Date(string = 'Date')
    amount_total = fields.Float(string = 'Total Amout')
    user_id = fields.Many2one('res.users', string = 'Sell Person')
    customer_ids = fields.Many2many('abc.customers', string = 'Customer')



