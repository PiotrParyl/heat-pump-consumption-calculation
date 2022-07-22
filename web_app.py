from flask import Flask, render_template
import mysql.connector
#======================= bd.connection #=======================

db = mysql.connector.connect(
    host="178.79.191.194",
    user="maczo_test",
    passwd="Pomidor123!@#",
    database="hotelowa_db",
)

mycursor = db.cursor()







#======================= Preparing Data #=======================

#=========== Value #===========

mycursor.execute("SELECT value FROM heat_pump ")
value_list = []

for i in range(0,11):
    for x in mycursor:
        value_list.append(x)




print (value_list)

#=========== Date #===========

date_list = []


mycursor.execute("SELECT date FROM heat_pump ")

for i in range(0,11):
    for x in mycursor:
        date_list.append(x)


print(date_list)



#======================= Web App #======================= 

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", value_kwh = joined )



if __name__==("__main__"):
    pass