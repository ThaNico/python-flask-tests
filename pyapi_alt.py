from flask import Flask, request, jsonify
from flask_restful import Api, Resource

print("Hello world 1")
print("Hello" + " " + "world 2")
print("Hello {} 3".format("world"))
print("Hello {0} 4".format("world"))
print("Hello {name} 5".format(name="world"))
name = "world"
print(f"Hello {name} 6")

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)


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

class Stock(Resource):
    
    def get(self):
        return stock, 200


api.add_resource(Stock, '/api/stock')

if __name__ == '__main__':
    app.run()