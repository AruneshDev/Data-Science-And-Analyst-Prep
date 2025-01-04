from dbmodule import connect
#Create connection object
connection = connect ('databasename','username','pswd')

# create a cursor object
cursor = connection.cursor()

# run queries
cursor.execute('select * from mytable')

results = cursor.fetchall()

# Free resources
cursor.close()
connection.close()