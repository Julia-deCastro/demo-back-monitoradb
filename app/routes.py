from flask import jsonify, request
from app import app, db
from app.models import Item
from app.validators import item_schema

@app.route('/')
def index():
    return jsonify(notification='Ok, server py is running!')

@app.route('/get_all_items', methods=['GET'])
def get_all_items():
    items = Item.query.all()
    item_list = [{"name": item.name, "idade": item.idade, "modalidade": item.modalidade } for item in items]
    return jsonify(items=item_list)

@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    errors = item_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    new_item = Item(name=data['name'], idade=data.get('idade'), modalidade=data.get('modalidade'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify(message='Item added successfully')
