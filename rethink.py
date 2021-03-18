#dependecies
from rethinkdb import r

#connecting to localhost
r.connect('localhost', 28015).repl()

#creating connection to the database 
connection = r.connect(db='DB_NAME')

#creating tables
r.table_create("table_name").run(connection)

variable = r.table("table_name")

#inserting into database
variable.insert({
    'id' : ---,
    'name' : ---,
    
}).run(connection)

#to print the database
for _ in variable.run(connection):
    print(_)