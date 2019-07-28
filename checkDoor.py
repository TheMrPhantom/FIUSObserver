
#!/usr/bin/env -S python3 -u

import requests
import os
import time
import subprocess
import datetime
import sys

#subprocess.run(["ls", "-l"])

fileName = "data/"
fileNumber = 1
commit = 0 if len(sys.argv) < 2 else sys.argv[1]


def checkDoor():
    r = requests.get("http://fius.informatik.uni-stuttgart.de/isOpen.php")
    # try:
    if r.text == "open":
        setDoorOpen(True)
    else:
        setDoorOpen(False)
    # except:
     #   print("Error")


def setDoorOpen(state):
    global commit
    subprocess.run(["git", "pull"])
    day = str(datetime.datetime.today().weekday())
    hour = datetime.datetime.today().hour
    minute = datetime.datetime.today().minute
    time = str(hour*60+minute)
    isOpen = str(1 if state else 0)
    f = open(fileName+str(fileNumber)+".txt", "a+")
    f.write(day+" "+time+" "+isOpen+"\n")
    f.close()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update "+str(commit)])
    subprocess.run(["git", "push"])
    print()
    commit = int(commit)+1


while True:
    checkDoor()
    time.sleep(60)
