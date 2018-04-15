from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "ketan@&*$singh"
api = Api(app)

jwt = JWT(app, authenticate, identity)	# /auth

items = []


class Item(Resource):
	"""	docstring for Item	"""
	@jwt_required()
	def get(self, name):
		# for item in items:
		# 	if item["name"] == name:
		# 		return item
		item = next(filter(lambda x: x['name'] == name, items), None)
		return {'item': item}, 200 if item is not None else 404

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None) is not None:
			return {"message": "Item with same name already exists"}, 400  

		data = request.get_json()
		item = {"name": name, "price": data['price']}
		items.append(item)
		return item, 201


class ItemList(Resource):
	"""docstring for ItemList"""
	def get(self):
		return {"items": items}

		

api.add_resource(Item, "/item/<string:name>", "/")
api.add_resource(ItemList, "/items")


if __name__=='__main__':
	app.run(debug=True)

# /items
# /item/<name>
# /item/<name>
# /item/<name>
# /item/<name>
