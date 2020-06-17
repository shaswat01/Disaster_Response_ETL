from flask import Flask

app = Flask(__name__)

from etl_app import routes