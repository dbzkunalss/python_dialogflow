from .db import db

class Order(db.Document):
    session = db.StringField(require = True, unique =True)
    products = db.ListField(db.StringField(), required=False, default = [])
    quantity = db.ListField(db.StringField(), required=False, default = [])