from socket  import *
from constCS import * #-
import re

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-

# Dicionario em que o grupo é a chave. Seu valor é uma lista de tuplas. Cada tupla é composta do nome de quem enviou a mensagem e do valor da mensagem.
dicionario = {}

# Definição do padrão da expressão regular
padrao = '\(\"(.*)\"\,\"(.*)\"\,\"(.*)\"\)'

(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
	data = conn.recv(1024)   # receive data from client

	if not data: break       # stop if client stopped

	# Separando os valores 1 - nome de quem enviou a mensagem, 2 - nome do grupo, 3 - mensagem enviada
	m = re.search(padrao,data.decode())

	# Se o grupo é novo
	if m.group(2) not in dicionario.keys():
		dicionario[m.group(2)] = []

	# Adicionando nova mensagem ao grupo
	dicionario[m.group(2)].append((m.group(1), m.group(3)))

	# Exibindo na tela as informações da última mensagem recebida
	print("grupo", m.group(2), dicionario[m.group(2)][-1][0], "disse:", dicionario[m.group(2)][-1][1])
	

	# print(m.groups())
	conn.send(m.group(3).encode()) # return sent data plus an "*"

conn.close()               # close the connection


