#!/usr/bin/python3
import random
import string
from flask import Flask
llist = string.ascii_lowercase
secrets={}

hostnames=['R610', '9020', '990', 'Home_Workstation']

try:
    secretsfile=open('./secrets.txt', 'r')
except:
    if len(hostnames)>0:
        secretsfile=open('./secrets.txt', 'a')
        print('Secrets file does not exist, generating secrets')
        for host in hostnames: 
            secrets[host]=(''.join(random.choice(llist) for i in range(20)))
        secretsfile.write(str(secrets))
    else:
        print("No hostnames, exiting...")
        exit()
app = Flask(__name__)

@app.route('/')
def slash():
    return

@app.route("/about")
def about_page():
  return "OK"


app.run(host="localhost", port=8000, debug=True)
