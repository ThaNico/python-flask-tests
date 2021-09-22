import flask

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

app.run()