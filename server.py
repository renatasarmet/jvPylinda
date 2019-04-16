from socket  import *
from constCS import * #-
import re
from linda.utils import bin_to_tuple

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-

# Dicionario em que o grupo é a chave. Seu valor é uma lista de tuplas. Cada tupla é composta do nome de quem enviou a mensagem e do valor da mensagem.
dicionario = {}

(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
	data = conn.recv(1024)   # receive data from client

	if not data: break       # stop if client stopped

	# Separando os valores 1 - nome de quem enviou a mensagem, 2 - nome do grupo, 3 - mensagem enviada
	matches = bin_to_tuple(data)

	for match in matches:
		(nome, grupo, mensagem) = match

		# Se o grupo é novo
		if grupo not in dicionario.keys():
			dicionario[grupo] = []

		# Adicionando nova mensagem ao grupo
		dicionario[grupo].append((nome, mensagem))

		# Exibindo na tela as informações da última mensagem recebida
		print("grupo", grupo, dicionario[grupo][-1][0], "disse:", dicionario[grupo][-1][1])
		

		# print(m.groups())
		# conn.send(mensagem.encode()) # return sent data plus an "*"

conn.close()               # close the connection


