from time import *
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
initial = True
timer = 0

while True:
    if initial is True:
        timer = 29
        initial = False

    sleep(0.5)
    timer += 1

    if timer == 30:
        f = open("email_comm.txt", "w")
        f.write("ready")
        f.close()

    f = open("email_comm.txt", "r+")
    email = f.readline()

    if email != "ready" and email != "true" and email != "false":
        f.seek(0)
        f.truncate()
        if re.fullmatch(regex, email):
            f.write("true")
        else:
            f.write("false")
        timer = 0

    f.close()
