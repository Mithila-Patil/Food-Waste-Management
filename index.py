from flask import *
from flask_mysqldb import MySQL
#from flask_mysql_connector import MySQL
import MySQLdb.cursors
import re

app=Flask(__name__)
app.secret_key="VCK"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='project'

mysql=MySQL(app)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/donor',methods=['POST','GET'])
def demo():
	if request.method=='POST':
		session['user_id']=request.form.get('user_id')
		session['city']=request.form.get('city')
		session['pass']=request.form.get('pass')

		user_id=session['user_id']
		city=session['city']
		password=session['pass']

		cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		
		cursor.execute("SELECT * FROM project.project_register WHERE pass=%s",(password,))

		data=cursor.fetchone()
		#if data:
		#	msg="Account already exists!"
		#elif not re.match(r'[A-Za-z0-9]+',user_id):
		#	msg="Username must contain only characters and numbers !"
		#elif not re.match(r'[A-Z]+',city):
		#	msg="City must contain only alphabets"
		#else:
		#	cursor.execute("INSERT INTO project.project_register1(user_id,city,pass) VALUES(%s,%s,%s)",(user_id,city,password))
		mysql.connection.commit()
		cursor.close()
	return render_template('donor.html')

@app.route('/donor',methods=['POST','GET'])
def demo1():
	#return render_template("donor.html")


	if request.method=='POST':
		user_id=session['user_id']
		city=session['city']
		password=session['pass']

		cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor=mysql.connection.cursor()
		cursor.execute("SELECT * FROM project.project_register WHERE pass= %s",(password))

		data=cursor.fetchone()
		#if data:
		#	msg="Account already exists!"
		#elif not re.match(r'[A-Za-z0-9]+',user_id):
		#	msg="Username must contain only characters and numbers !"
		#elif not re.match(r'[A-Z]+',city):
		#	msg="City must contain only alphabets"
		#else:
		#	cursor.execute("INSERT INTO project.project_register1(user_id,city,pass) VALUES(%s,%s,%s)",(user_id,city,password))
		mysql.connection.commit()
		cursor.close()
		return render_template('donor.htmL')


@app.route('/receiver',methods=['POST','GET'])
def demo2():
	if request.method=='POST':
		session['user_id']=request.form.get('user_id')
		session['city']=request.form.get('city')
		session['pass']=request.form.get('pass')

		user_id=session['user_id']
		city=session['city']
		password=session['pass']

		cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		
		cursor.execute("SELECT * FROM project.project_register1 WHERE pass=%s",(password,))

		data=cursor.fetchone()
		#if data:
		#	msg="Account already exists!"
		#elif not re.match(r'[A-Za-z0-9]+',user_id):
		#	msg="Username must contain only characters and numbers !"
		#elif not re.match(r'[A-Z]+',city):
		#	msg="City must contain only alphabets"
		#else:
		#	cursor.execute("INSERT INTO project.project_register1(user_id,city,pass) VALUES(%s,%s,%s)",(user_id,city,password))
		mysql.connection.commit()
		cursor.close()
	return render_template("receiver.html")

@app.route('/receiver',methods=['POST','GET'])
def demo3():
	if request.method=='POST':
		user_id=session['user_id']
		city=session['city']
		password=session['pass']

		cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor=mysql.connection.cursor()
		cursor.execute("SELECT * FROM project.project_register1 WHERE pass= %s",(password))

		data=cursor.fetchone()
		#if data:
		#	msg="Account already exists!"
		#elif not re.match(r'[A-Za-z0-9]+',user_id):
		#	msg="Username must contain only characters and numbers !"
		#elif not re.match(r'[A-Z]+',city):
		#	msg="City must contain only alphabets"
		#else:
		#	cursor.execute("INSERT INTO project.project_register1(user_id,city,pass) VALUES(%s,%s,%s)",(user_id,city,password))
		mysql.connection.commit()
		cursor.close()
	return render_template("receiver.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/gallery')
def gallery():
	return render_template("gallery.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/foodid')
def food():
	return render_template("foodid.html")


@app.route('/formdonor',methods=['POST','GET'])
def demo4():
	if request.method=='POST':
		session['name']=request.form['name']
		session['city']=request.form['city']
		session['phone']=request.form['phone']
		session['adderess']=request.form['adderess']
		session['food_info']=request.form['food_info']
		session['quantity']=request.form['quantity']
		session['pick_up_date']=request.form['pick_up_date']

		name=session['name']
		city=session['city']
		phone=session['phone']
		adderess=session['adderess']
		food_info=session['food_info']
		quantity=session['quantity']
		pick_up_date=session['pick_up_date']
		

		cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("INSERT INTO project.project_register11(name,city,phone,adderess,food_info,quantity,pick_up_date) VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,city,phone,adderess,food_info,quantity,pick_up_date))
		mysql.connection.commit()
		cursor.close()
	return render_template("formdonor.html")

@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
	cursor=mysql.connection.cursor()
	cursor.execute("select * from project.project_register11")
	data=cursor.fetchall()
	return render_template("dashboard.html",data=data)


