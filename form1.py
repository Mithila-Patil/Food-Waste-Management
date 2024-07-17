from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def form1():
	return render_template('.html')
