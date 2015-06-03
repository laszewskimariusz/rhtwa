### RPi Temp and Humidity Windows App RTHWA 0.1
### Created by Mariusz Laszewski

from tkinter import *
import sys
import mysql.connector

Root=Tk()
RTitle=Root.title("RTHWA 0.1")

Root.geometry("800x600")
Root.wm_iconbitmap("n.ico")

### Mysql login

cur = mysql.connector.connect(user="mariusz", password="shinigami", host ="192.168.0.12", database="dht")
cursor = cur.cursor()


cursor.execute( "SELECT * FROM temp ORDER BY id DESC LIMIT 0 , 1" )

#cursor.execute("SELECT * FROM temp ")

data = cursor.fetchall()
for row in data:
    print (row[3], row[4], row[2]) # liczymy row od 0
cursor.close()

Label(Root, text=("Temperature:"), font="Times 40").pack()
Label(Root, text=(row[4]),fg = "red", bg = "blue", font="Times 40").pack()
     
Label(Root, text=("Humidity"), font="Times 40").pack()
Label(Root, text=(row[3]),fg = "red", bg = "blue", font="Times 40").pack()

Label(Root, text=("Last update"), font="Times 10").pack()
Label(Root, text=(row[2]),fg = "red", bg = "blue", font="Times 10").pack()




Root.mainloop()
