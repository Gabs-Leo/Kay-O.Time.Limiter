import os
import datetime
from time import sleep

while True:
    now = datetime.datetime.now()
    if now.hour >= 18:
        os.system("shutdown /s /t 1")
        sleep(5)
    else:
        print("Waiting to Strike")
        sleep(5)