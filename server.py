from socket  import *
from constCS import * #-
import re

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-

#dict = {}

padrao = '\(\"(.*)\"\,\"(.*)\"\,\"(.*)\"\)'

(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
	data = conn.recv(1024)   # receive data from client

	if not data: break       # stop if client stopped
  #if data[1] not in dict.keys():
  	#dict[data[1]] = (data[0], data[2])
  #print("grupo : ", dict[data[1]].key(), dict[data[1]][0], " disse ", dict[data[1]][2])
	m = re.search(padrao,data.decode())

	print(m.groups())
	conn.send(m.group(1).encode()) # return sent data plus an "*"
conn.close()               # close the connection


