from odoo import fields, models


class ExampleModel(models.Model):
  _name = 'example.model'

  name = fields.Char()
  number_integer = fields.Integer()
  number_float = fields.Float()
