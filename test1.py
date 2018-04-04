from flask import Flask, request, url_for

app = Flask(__name__)


@app.route("/index")
def index():
	pass

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    print(url_for('index'))


print(__name__)
