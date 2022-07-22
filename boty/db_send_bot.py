import minimalmodbus
import serial
from time import sleep
import datetime
from datetime import datetime
import mysql.connector


#========================= db.connection #=========================

db = mysql.connector.connect(
    host="178.79.191.194",
    user="maczo_test",
    passwd="Pomidor123!@#",
    database="hotelowa_db",
)

mycursor = db.cursor()




#========================= licznik connection #=========================
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 3)  # port name, slave address (in decimal)

instrument.serial.port                     # this is the serial port name
instrument.serial.baudrate = 9600         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 0.1          # seconds
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
instrument.clear_buffers_before_each_transaction = True


# print(instrument)


#========================= loop #=========================
while True:
        r0 = instrument.read_register(0)


        sleep(1)



        r1 = instrument.read_register(1)


        sleep(2)


        r2 = instrument.read_register(2)


        wynik = (r0 *(256*256) + r1 * 256 + r2)/10

        print (wynik)

        e = datetime.now()

        print (e)

        #========================= dodawanie do bazy danych #=========================







        mycursor.execute("SELECT value FROM heat_pump ")


        test_list = []
        for x in mycursor:




                test_list.append(x)



        value= list(f"{test_list[-1]}")

        del value[0:2]
        del value[-3:-1]
        del value[-1]
        joined = "".join(value)

        print(joined)
        test_list*=0


        wynik = str(wynik)
        joined = str(joined)


        if wynik == joined:
                print ("wunik ten sam nie dodaje do bazy ")

        else:
                print("Dodaje do bazy")

                mycursor.execute("INSERT INTO heat_pump (value,date) VALUES(%s,%s)",  (wynik,e))


        db.commit()


        sleep(60)





