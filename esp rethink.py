#dependencies
import socket 
import time 
from rethinkdb import r

#rethink database connector
r.connect('localhost',28015).repl()


#to create new databases
connection = r.connect(db = "ESP32")

# to create tables
# r.table_create("MPU_GYRO").run(connection)
# r.table_create("VIBRATION").run(connection)
# r.table_create("TEMPERATURE").run(connection)

#socket connection
s=socket.socket()
s.bind(('0.0.0.0',5767))
s.listen(5)


while True:
    Time = round(time.time() * 1000) #timeseries in milliseconds
    c,addr = s.accept()
    
    data = c.recv(1024).decode("utf-8") #receiving and decoding data 
    DATA = data.split()
    print(DATA)
    
    
    #inserting into first table
    r.table('MPU_GYRO').insert(r.expr({
        'id':Time,
        'GyroX':DATA[4],
        'GyroY':DATA[5],
        'GyroZ':DATA[6],
    })).run(connection)
    
     #inserting into second table
    r.table('VIBRATION').insert({
        'id':Time,
        "Vibration":"NONE",
    }).run(connection)
    
     #inserting into third table
    r.table('TEMPERATURE').insert({
        'id':Time,
        'Temperature':DATA[0],
    }).run(connection)
    
    #delay in code for better and accyrate database
    time.sleep(1)
    
    print("RECORD INSRTED")
  