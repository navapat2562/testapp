from odoo import models, fields


class ModelName(models.Model):
    _name = 'estate.property'
    _description = 'This is test'

    name = fields.Char("Title", required=True)
    age = fields.Char("Ages")
    number = fields.Char("Number")


