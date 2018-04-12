from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


stores = [
    {
        "name": "my amazing store",
        'items': [
            {
                "name": "toothpaste",
                        "price": 49
            },
        ]
    },
]


# return all the stores
@app.route('/stores')
def get_all_stores():
    return jsonify({"stores": stores})


# create a new store
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


# get some store
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# returns all items inside a perticular store:name
@app.route("/store/<string:name>/items")
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


# create items in store
@app.route("/store/<string:name>/item", methods=['POST'])
def create_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }

            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'Error adding items. Store not found!'})


app.run()
