import mysql.connector

mydatadatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "university_db"
)

testnet = mydatadatabas.cursor() 

    testnet.execute("""
            CREATE TABLE IF NOT EXISTS `Api_information`(
                `country` VARCHA(100),
                `Domain` VARCHA(100),
                `alpha_code`VARCHA(100),
                `state` VARCHA(100),
                `web` VARCHA(100),
                `Names` VARCHA(100)
            );
         """)