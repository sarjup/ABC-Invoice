from odoo import models, fields, api

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

    number = fields.Char(string = 'Bill No.', required = True)
    vendor_ids = fields.Many2one('abc.vendors',string = 'Vendor', required = True)
    bill_line_ids = fields.One2many('abc.product.bill.line', 'purchase_id', string = 'Bill Line')
    date_purchase = fields.Date(string='Date')
    user_id = fields.Many2one('res.users',string = 'Entry Person')
    amount_total = fields.Float(string = 'Total', compute = '_compute_amount', store = True )
    display_name = fields.Char(compute = '_compute_display_name')

    @api.depends('number')
    def _compute_display_name(self):
        for vendor_bill in self:
            vendor_bill.display_name = vendor_bill.number
    
    @api.multi
    @api.depends('bill_line_ids.amount_product')
    def _compute_amount(self):
        self.ensure_one()
        self.amount_total = sum(line.amount_product for line in self.bill_line_ids )    



class ProductInvoiceLine(models.Model):
    _name = "abc.product.bill.line"
    _description = "Product Purchase invoice line"

    product_ids = fields.Many2one('abc.products', required = True, string = "Product")
    description = fields.Char(string = "Description", required = True)
    amount_product = fields.Float(string = "Amount",compute = '_compute_product_amount', store= True)
    amount_cost = fields.Float(string = "Cost Price", required = True)
    amount_sale = fields.Float(string = "Sale Price", required = True)
    quantity_product = fields.Float(string = "Quantity")
    purchase_id = fields.Many2one('abc.purchase.bill', string = "Purchase")

    @api.onchange('product_ids')
    def _onchange_product_id(self):
        product = self.product_ids

        self.description = product.description
        self.amount_cost = product.standard_price
        self.amount_sale = product.list_price

    @api.multi
    @api.depends('amount_cost','quantity_product')
    def _compute_product_amount(self):
        for product in self:
            product.amount_product = product.amount_cost * product.quantity_product
            


