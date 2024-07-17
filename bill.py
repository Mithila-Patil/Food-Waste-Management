from flask import Flask,render_template
#from flask_mysql_connector import MySQL 
#from flask_mysqldb import MySQL

app=Flask(__name__)
#app.secret_key="ABC"

#app.config['MYSQL_HOST']='localhost'
#app.config["MYSQL_USER"]='root'
#app.config["MYSQL_PASSWORD"]='12345'
#app.config["MYSQL_DB"]='db'
#mysql=MySQL(app)

@app.route('/<int:bill_no>/<int:consumer_no>/<int:previous_unit>/<int:current_unit>')
def home(bill_no,consumer_no,previous_unit,current_unit):
	
	return render_template("bill.html",bno=bill_no,cno=consumer_no,pu=previous_unit,cu=current_unit)