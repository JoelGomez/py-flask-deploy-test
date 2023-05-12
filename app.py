from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    """funcion para verificar que el servidor corra bien"""
    print("Pepe el toro es inocente")