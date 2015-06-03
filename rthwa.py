### RPi Temp and Humidity Windows App RTHWA 0.1
### Created by Mariusz Laszewski
#
# Python 3.4.3 required 
#
# mysql-connector need to be instaled
# Download page http://dev.mysql.com/downloads/file.php?id=457172
# 
#

from tkinter import *
import sys
import mysql.connector
import configparser


config = configparser.ConfigParser()
Root = Tk()
menubar = Menu(Root)
RTitle=Root.title("RTHWA 0.1")

Root.geometry("800x600")
Root.wm_iconbitmap("n.ico")


def bum():
   filewin = Toplevel(Root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
def about():
   filewin = Toplevel(Root)
   label = Label(filewin, text="RPi Temp and Humidity Windows App RTHWA 0.1" '\n' "Created by Mariusz Laszewski" '\n' "mariuszlaszewski@gmail.com")
   label.pack()
def editconf():
    from subprocess import call
    call("notepad config.ini")
    

### menubar section

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Connect", command=bum)
filemenu.add_command(label="Open config.ini", command=editconf)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=Root.destroy)

menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

Root.config(menu=menubar)



### Config file

config.read('config.ini')
mysqluser = config.get('MYSQL CONFIG', 'User')
mysqlpass = config.get('MYSQL CONFIG', 'Password')
mysqlhost = config.get('MYSQL CONFIG', 'Host')
mysqldata = config.get('MYSQL CONFIG', 'Database')


### Mysql login

cur = mysql.connector.connect(user = (mysqluser) , password = (mysqlpass), host = (mysqlhost), database = (mysqldata))

cursor = cur.cursor()


cursor.execute( "SELECT * FROM temp ORDER BY id DESC LIMIT 0 , 1" )



data = cursor.fetchall()
for row in data:
    print (row[3], row[4], row[2]) # counting Row from 0
cursor.close()



## Label section 

Label(Root, text=("Temperature:"), font="Times 40").pack()
Label(Root, text=(row[4]),fg = "red", bg = "blue", font="Times 40").pack()
     
Label(Root, text=("Humidity"), font="Times 40").pack()
Label(Root, text=(row[3]),fg = "red", bg = "blue", font="Times 40").pack()

Label(Root, text=("Last update"), font="Times 10").pack()
Label(Root, text=(row[2]),fg = "red", bg = "blue", font="Times 10").pack()


#####################
Root.mainloop()



