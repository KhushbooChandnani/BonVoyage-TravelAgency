from datetime import date
import mysql.connector

        
	

def create_connect():
        global conn
        conn = mysql.connector.connect(user="admin",password="",host="localhost",database="bonvoyage")
        global cursor
        cursor = conn.cursor()

def signin_data(uname,passwrd) :
        create_connect()
        query = "SELECT * FROM `customers`"
        cursor.execute(query)
        row = cursor.fetchall()
        #print(row)
        for i in range(len(row)):
                #print(row)
                if(row[i][1]==uname):
                        #print(pass_row)
                        if(row[i][2] == passwrd) :
                                cursor.close()
                                conn.close()
                                return 1
                #row = cursor.fetchone()
        cursor.close()
        conn.close()
        return 0
        

def register_data(usrname,email,password):
        create_connect()
        query = "INSERT INTO customers (Email_id, Password, Name) VALUES ('%s','%s','%s')"%(email,password,usrname)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        return 1


        
def rentCal(x,y,z,name,pax,flight):
        create_connect()
        query = "Select * from rate_chart"
        cursor.execute(query)
        row = cursor.fetchall()
        for i in range(len(row)):
                if row[i][1] == name:
                        rate = int(row[i][pax+1])
                        flightFare = int(row[i][6])
                        rent =  [((y-x).days*rate*z) , (flight*pax*flightFare)]
                        cursor.close()
                        conn.close()
                        return rent


def booking_data(hotelName,guestName,inDate,outDate,roomCount,guestCount,total):
        create_connect()
        query = "INSERT INTO bookings(Name_of_hotel, Name_of_guest, Check_in_date, Check_out_date, No_of_rooms, Pax_per_room, Amount_to_be_paid) VALUES ('%s','%s','%s','%s','%s','%d','%d')"%(hotelName,guestName,str(inDate),str(outDate),roomCount,guestCount,total)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        return 1