from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
from linda.utils import bin_to_tuple

class ServerThread(Thread):
    def __init__(self, HOST, PORT):
        Thread.__init__(self)
        self.sck = socket(AF_INET, SOCK_STREAM) 
        self.sck.bind((HOST, PORT))  #-
        self.conn = None
        self.addr = None

    def run(self):
        while True:
            self.sck.listen(1)           #-

            (self.conn, self.addr) = self.sck.accept()  # returns new socket and self.addr. client 
            dicionario = {}
            print("running server socket =D")
            data = self.conn.recv(1024)   # receive data from client

            if not data: return       # stop if client stopped

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
                self.conn.send(mensagem.encode()) # return sent data plus an "*"

    def __del__(self):
        if self.conn:
            self.conn.close()               # close the self.connection
        self.join()


def create_server(HOST=None, PORT=None):
    """
        Faz da máquina que chama essa função o servidor
    """
    server_thread = ServerThread(HOST=HOST, PORT=PORT)
    server_thread.start()
