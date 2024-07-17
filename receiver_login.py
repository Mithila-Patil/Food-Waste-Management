from flask import *
from flask_mysqldb import MySQL 

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='mithila'
app.config['MYSQL_DB']='food'

MySQL=MySQL(app)

query="INSERT INTO food(user_id,rname,city,pass) VALUES(%s,%s,%s,%s)"
val=(2,'mithila','kolhapur','abc@123')

@app.route('/')
def create_table():
	cursor=mysql.connection.cursor()
	cursor.execute(query,val)
	mysql.connection.commit()
	cursor.close()
	return"record is inserted"
