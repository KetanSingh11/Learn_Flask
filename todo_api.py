from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todo = {}

class myTodo(Resource):
	"""
	docstring for myTodo
	"""
	def get(self, name):
		return jsonify({"data": "Hello {}".format(name)})


api.add_resource(myTodo, "/hello/<string:name>")

if __name__=='__main__':
	app.run(debug=True)



# /items
# /item/<name>
# /item/<name>
# /item/<name>
# /item/<name>
