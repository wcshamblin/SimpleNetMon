#!/usr/bin/python3
import os
import base64

rserv='will@shamblin.org'
hostname='home_workstation' #do not use commas, that is the delim
phost='google.com'

pcache=[]
cping=os.popen('ping -c 10 -W 5 ' + phost).read().strip().split('\n')
for row in cping[1:-4]:
    try:
        pcache.append((float(row.split(' ')[-2].split('=')[1])))
    except:
         pcache.append(0.0)
pcache=[round(round(sum((pcache)), 2)/len(pcache), 2)]

print("SimpleNetMonHostname="+str(hostname)+",Ping="+str(pcache[0]))
