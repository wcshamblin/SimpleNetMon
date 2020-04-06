#!/usr/bin/python3
import random
import string
from flask import Flask
llist = string.ascii_lowercase
secrets={}

hostnames=['R610', '9020', '990', 'Home_Workstation']


def secretreturn(secret):
    return(secret)

try:
    secretsfile=open('./secrets.txt', 'r+')
    for line in secretsfile:
        (host, secret) = line.split(',')
        secrets[host]=secret
    shosts=[item[0] for item in secrets.items()]
    if set(hostnames) != set(shosts):
        if len(hostnames) > len(shosts):
            for host in list(set(hostnames)-set(shosts)):
                secretsfile.write(str(host)+','+(''.join(random.choice(llist) for i in range(20)))+'\n')
except IOError:
    if len(hostnames)>0:
        secretsfile=open('./secrets.txt', 'a')
        secretsfile.seek(0)
        print('Secrets file does not exist, generating secrets')
        for host in hostnames: 
            secrets[host]=(''.join(random.choice(llist) for i in range(20)))
        for hostname, secret in secrets.items():
            secretsfile.write(str(hostname)+','+str(secret)+'\n')
    else:
        print("No hostnames, exiting...")
        exit()
app = Flask(__name__)

@app.route('/')
def slash():
    return('OK')

for secret in secrets:
    app.add_url_rule('/'+secret, secret, secretreturn)

app.run(host='0.0.0.0', port=8000)
