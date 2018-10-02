from shops_app import app
from flask import render_template


@app.route('/')
def index():
	return '<h1>HEllo</h1>'

