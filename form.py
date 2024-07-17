from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def form():
	return render_template('salaryform1.html')

@app.route('/data',methods=['POST','GET'])
def data():
	if request.method=='POST':
		data=request.form.to_dict()
		s=int(request.form['salary'])
		m=str(request.form['designation'])
		return render_template('salarydata.html',form_data=data,sal=s,design=m)