import os
import datetime
from time import sleep

#Hora em que o computador desligará
#Hour that will shutdown the computer
shutdown = 18

#Checagem de horário infinita
#Infinity time check
while True:
    now = datetime.datetime.now()
    if now.hour >= shutdown:
        os.system("shutdown /s /t 1")
        sleep(5)
    else:
        print("Waiting to Strike")
        sleep(5)