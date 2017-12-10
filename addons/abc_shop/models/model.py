from odoo import models, fields

class Customers(models.Model):
    _name = "abc.customers"
    _description = "This model is for customers of ABC shop"

    name = fields.Char(string="Name", required = True)
    address = fields.Char(string = "Address")
    email = fields.Char(string = "Email")
    contact = fields.Char(string="Phone", required = True)
    type = fields.Selection([
        ('normal','Normal'),
        ('reguler','Reguler'),
        ('special','Special')],
        string = "Customer Type",
        default = "normal")
    active = fields.Boolean(string = "Active?", default = True)


class Vendors(models.Model):
    _name = "abc.vendors"
    _description = "this model is for vendors of ABC Shop"

    name = fields.Char(string = "Name", required =True)
    address = fields.Char(string = "Address")
    email = fields.Char(string = "Email")
    contact = fields.Char(string="Phone", required = True)
    type = fields.Selection([
        ('normal','Normal'),
        ('reguler','Reguler'),
        ('special','Special')],
        string = "Customer Type",
        default = "normal")
    active = fields.Boolean(string = "Active?", default = True)


class Products(models.Model):
    _name = "abc.products"
    _description = "this model specifies the products for the ABC Shop"

    name = fields.Char(string = "Product Name", required = True)
    description = fields.Text('Description')
    type = fields.Selection([
        ('consumable','Consumable'),
        ('service','Service')
        ],
        string = 'Product Type',
        default = 'consumable')
    qty_product = fields.Float(string="Quantity")
    list_price = fields.Float(string = "Sale Price")
    standard_price = fields.Float(string="Cost Price")
    active = fields.Boolean(string = "Active?", default = True)


class PurchaseInvoice(models.Model):
    _name = 'abc.purchase.bill'
    _description = 'Product Purchase Wizard'

    number = fields.Char(string = 'Bill No.')
    vendor_ids = fields.Many2one('abc.vendors',string = 'Vendor')
    product_ids = fields.Many2many('abc.products', string = 'Product')
    date_purchase = fields.Date(string='Date')
    user_id = fields.Many2one('res.users',string = 'Entry Person')
    amount_total = fields.Float(string = 'Total')
