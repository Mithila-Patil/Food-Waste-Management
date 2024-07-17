from flask import Flask,render_template
app=Flask(__name__)

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/style')
def style():
	return render_template("style.css")