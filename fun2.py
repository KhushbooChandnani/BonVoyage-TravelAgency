import mysql.connector


def create_connect():
        global conn
        conn = mysql.connector.connect(user="admin",password="",host="localhost",database="bonvoyage")
        global cursor
        cursor = conn.cursor()


def rentCal(x = None,y = None,z=1,name = None,pax =):
	create_connect()
	query = "Select * from rate_chart"
	args = (name)
	cursor.execute(query)
	row = cursor.fetchall()
	for i in range(len(row)):
		if row[i][1] == name:
			rate = int(row[i][pax])
			return ((y.day - x.day)*rate*z)
	
	
