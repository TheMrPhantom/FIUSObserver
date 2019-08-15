#!/usr/bin/env -S python3 -u

import requests
import time
import subprocess
import sys
from datetime import datetime, timedelta


base_path = "data/"
file_name = 3 if len(sys.argv) < 2 else sys.argv[1]
next_commit_time = datetime.datetime.now()


def check_door_state():
    try:
        r = requests.get("http://fius.informatik.uni-stuttgart.de/isOpen.php")
    
        if r.text == "open":
            log_door_state(True)
        else:
            log_door_state(False)
    except:
        print("Error")


def produce_textual_data_point(is_open):
    day = str(datetime.datetime.today().weekday())
    hour = datetime.datetime.today().hour
    minute = datetime.datetime.today().minute
    time = str(hour * 60 + minute)
    openness_state = str(1 if is_open else 0)
    return day + " " + time + " " + openness_state + "\n"


def produce_binary_data_point(is_open):
    timestamp = datetime.datetime.today().timestamp()
    return tuple(timestamp, is_open)


def commit_data():
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update " + str(datetime.datetime.now())])
    subprocess.run(["git", "push"])


def log_door_state(is_open):
    global next_commit_time

    f = open(base_path + str(file_name) + ".txt", "a+")
    f.write(produce_textual_data_point(is_open))
    f.close()
    if datetime.datetime.now() > next_commit_time:
        commit_data()
        next_commit_time = datetime.datetime.now() + timedelta(hours=12)
        print()


time.sleep(10)
check_door_state()

while True:
    check_door_state()
    time.sleep(60)
