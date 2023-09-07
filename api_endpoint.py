import requests 
import mysql.connector

# endpoint_url = "https://jsonplaceholder.typicode.com/todos"
# app_create = {
#     "userId":20,
#     "Id": 400,
#     "title":"the home of valour",
#     "completed": True
# }
# feedback = requests.post(endpoint_url, json=app_create)
# print(feedback.json())
# print(feedback.status_code)
# ________________________________________________________________________________________________________________
# Exercise on jasonPlaceholder 

# end_db = "https://jsonplaceholder.typicode.com/photos"
# app_create = {
#     "AlbumId" : 100,
#     "Id" : 5000,
#     "title": "My Photo",
#     "url": "https://via.placeholder.com/600/6dd9cb",
#     "thumbnailUrl":"https://via.placeholder.com/150/6dd9cb",
# }
# checkback = requests.get(end_db, json=app_create)
# print(checkback.json())
# print(checkback.status_code)

# check = requests.post(end_db, json=app_create)
# print(check.json())
# print(check.status_code)

# creating databases
db_conn = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "",
    db = 'endpoint_db'
)
mycursor = db_conn.cursor()
if db_conn.is_connected():
    # mycursor.execute("CREATE DATABASE IF NOT EXISTS `endpoint_db`")
    # mycursor.execute("USE endpoint_db")
    mycursor.execute('''CREATE TABLE IF NOT EXISTS `placeholder_table`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(300),
    `url` VARCHAR(300),
    `thumbnailUrl` VARCHAR(300)
    )
    ''')
    print("table created successfully ")

db_conn.commit()
db_conn.close()


