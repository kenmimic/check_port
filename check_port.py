#!/usr/bin/env python3
import sys,time,re,socket,datetime

ip=sys.argv[1]
port=int(sys.argv[2])
bytes_recd = 0
data = None

def check_port():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #while data is none:
    for count in range(0,1000,1):
    # try creating a socket to target ip or print msg  
      try:
        s.connect((ip,port))
        data = s.recv(1024)
        if data:
          print("Port %s/tcp open" %str(port))
          print(datetime.datetime.now())
      except socket.error as msg:
            sys.stdout.write("\r")
            sys.stdout.write("{:4d} retry 5 seconds".format(count))
            sys.stdout.write(str(msg))
            sys.stdout.flush()
            time.sleep(5)
    check_port()

check_port()
