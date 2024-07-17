from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
#from flask_mysql_connector import MySQL 

app=Flask(__name__)
app.secret_key='mmm'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='mysql'
mysql=MySQL(app)

@app.route('/home', methods=['POST','GET'])
def home():
	data=""
	if request.method=="POST":
		cust_no=request.form['cust_no']
		#cust_name=request.form['cust_name']
		sex=request.form['sex']
		birthdate=request.form['birthdate']
		country=request.form['country']
		state=request.form['state']
		address=request.form['address']
		pincode=request.form['pincode']
		m_no=request.form['m_no']
		email=request.form['email']
		cursor=mysql.connection.cursor()
		cursor.execute("INSERT INTO mysql.customer(cust_no,sex,birthdate,country,state,address,pincode,m_no,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cust_no,sex,birthdate,country,state,address,pincode,m_no,email,))
		mysql.connection.commit()	
		cursor.close()
	return render_template("q1.html",data=data)