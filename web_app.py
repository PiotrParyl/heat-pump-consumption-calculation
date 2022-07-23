from posixpath import split
from flask import Flask, render_template
import mysql.connector
from setings import *
#======================= bd.connection #=======================

db = mysql.connector.connect(
    host= host,
    user=user,
    passwd=passwd,
    database=database,
)

mycursor = db.cursor()







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


#=========== Date #===========
data_test_list = []
date_list = []
hour_list = []


mycursor.execute("SELECT date FROM heat_pump ")


for x in mycursor:
    data_test_list.append(x)

for i in range(1,11):
    value = list(f"{data_test_list[-i]}")
    
    del value[0:2]
    del value[-3:]
    del value[10:]
    joined = "".join(value)
    date_list.append(joined)

for i in range(1,11):
    value = list(f"{data_test_list[-i]}")
    
    del value[0:13]
    del value[-10:]
    
    joined = "".join(value)
    hour_list.append(joined)


print(hour_list)





#=========== Cuda na kiju  #===========

for i in value_list:
    i = float(i)
    value_list_float.append(i)

for i in range(0,9):
    b = value_list_float[i]-value_list_float[i+1]
    kw.append(b)



    





#======================= Web App #======================= 

app = Flask(__name__)


@app.route('/')
def home():

    


        
    data = [
        (f"{date_list[0]}",kw[0]),
        (f"{date_list[1]}",kw[1]),
        (f"{date_list[2]}",kw[2]),
        (f"{date_list[3]}",kw[3]),
        (f"{date_list[4]}",kw[4]),
        (f"{date_list[5]}",kw[5]),
        (f"{date_list[6]}",kw[6]),
        (f"{date_list[7]}",kw[7]),
        (f"{date_list[8]}",kw[8]),
        

    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("home.html", labels=labels, values=values  )



if __name__==("__main__"):
    pass
    #app.run(debug=True)