from ast import Return
import os, sys
import sqlite3
import numpy as np


## Database
## Host DB File
hostCon = sqlite3.connect('hosts.db')
hostCur = hostCon.cursor()


def pingHosts():    
    queryDbForHosts = hostCur.execute("SELECT ipAddr FROM hosts")
    ipToScan = queryDbForHosts.fetchall() # Returns Tuple, not array
    arr = np.asarray(ipToScan)


    for hosts in arr:
        response = os.system("ping -c 1 " + hosts)

        if response == 0:
            print (hosts, 'is up!')
        else:
            print (hosts, 'is down!')

pingHosts()



