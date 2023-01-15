from flask import Flask
from example_blueprint import example_blueprint

app = Flask(__name__)

#Blueprint registration
app.register_blueprint(example_blueprint)