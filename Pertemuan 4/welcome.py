from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def home():
    return "Welcome Back Brooow!"

app.run()