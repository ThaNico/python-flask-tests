import flask
from flask import request, jsonify

print("Hello world 1")
print("Hello" + " " + "world 2")
print("Hello {} 3".format("world"))
print("Hello {0} 4".format("world"))
print("Hello {name} 5".format(name="world"))
name = "world"
print(f"Hello {name} 6")

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World</h1>"
    
    
stock = [
    {'id': 0,
     'product': 'corde',
     'stock': 42},
    {'id': 1,
     'product': 'baudrier',
     'stock': 0}
]

@app.route('/api/stock/all', methods=['GET'])
def api_show_all_stock():
    return jsonify(stock)



app.run()