from posixpath import split
from flask import Flask, render_template
import mysql.connector
from setings import *

db = mysql.connector.connect(
    host= host,
    user=user,
    passwd=passwd,
    database=database,
)

mycursor = db.cursor()

app = Flask(__name__)

@app.route('/')
def home():

    #======================= Preparing Data #=======================

    #=========== Value #===========

    mycursor.execute("SELECT value FROM heat_pump ")


    test_list = []
    value_list = []
    value_list_float = []
    kw = []


    for x in mycursor:
        test_list.append(x)


    for i in range(1,11):
        value= list(f"{test_list[-i]}")

        del value[0:2]
        del value[-3:-1]
        del value[-1]
        joined = "".join(value)

        value_list.append(joined)







    for i in range(0,11):    
        data = [

            ("chuj",i),
            
            
            

        ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("home.html", labels=labels, values=values  )



if __name__==("__main__"):
    app.run(debug=True)