from ast import Return
import os, sys
import sqlite3


## Database
## Host DB File
hostCon = sqlite3.connect('hosts.db')
hostCur = hostCon.cursor()

hostCur.execute("SELECT * FROM hosts")
rows = hostCur.fetchall()
for hosts in rows:
    response = os.system("ping -c 1 " + hosts)

    if response == 0:
        print (hosts, 'is up! cool')
    else:
        print (hosts, 'is down!')

# Working Ping


