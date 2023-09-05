from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://monitoradb:3YZFEp5Z6GJpA6BNGlTqDDPNGma8BInf@dpg-cis2uvdph6et1sd86n8g-a.oregon-postgres.render.com/monitoradb'
db = SQLAlchemy(app)
CORS(app)

from app import routes
