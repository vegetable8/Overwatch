from ast import Return
import os, sys
import sqlite3


## Database
## Host DB File
hostCon = sqlite3.connect('hosts.db')
hostCur = hostCon.cursor()

### Functions
def dbCreate():
    print('Provisioning Host Database, beep boop.')
    try: 
        f = open("hosts.db", "x")
    except: 
        pass
    hostCur.execute('''CREATE TABLE hosts
                    (ipAddr, friendlyName)''')
    hostCon.commit()
    hostCon.close()
    print('beep, boop. Database has been created.')

def hostCreate():
    frenInput = input("Friendly Name: ")
    hostnameInput = input("Hostname/IP Address: ")
    print('Adding a host, beep boop.')
    hostCur.execute("INSERT INTO hosts (ipAddr,friendlyName) VALUES ('"+hostnameInput+"','"+frenInput+"')")
    hostCon.commit()


### CLI Args
arg1 = sys.argv[1]

### DATABASE CREATION
if sys.argv[1] == '--dbcreate':
    dbCreate()

elif arg1 == '--addhost':
    hostCreate()

elif arg1 == '--showDb':
    hostCur.execute("SELECT * FROM hosts")

    rows = hostCur.fetchall()

    for row in rows:
        print(row)
