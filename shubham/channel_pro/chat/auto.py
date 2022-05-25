# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
password =""
)

print(dataBase)

# Disconnecting from the server
dataBase.close()
