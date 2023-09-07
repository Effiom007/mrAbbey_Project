https://github.com/Effiom007/class_exercise.git

test = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    
)

testing = test.cursor()
if (testing):
    testing.execute("CREATE DATABASE IF NOT EXIST `university_db`")
    print("database created")

else:
    print("database not connected")



