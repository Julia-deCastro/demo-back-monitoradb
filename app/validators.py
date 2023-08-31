from marshmallow import Schema, fields, validate

class ItemSchema(Schema):
    name = fields.Str(required=True)
    idade = fields.Str(required=True)
    modalidade = fields.Str(required=True)

item_schema = ItemSchema()
