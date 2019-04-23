from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
from linda.utils import bin_to_tuple, list_to_bin

class ServerThread(Thread):
    def __init__(self, HOST, PORT):
        Thread.__init__(self)
        self.sck = socket(AF_INET, SOCK_STREAM) 
        self.sck.bind((HOST, PORT))  #-
        self.conn = None
        self.addr = None
        self.dictionary = {}

    def run(self):
        while True:
            self.sck.listen(1)           #-

            (self.conn, self.addr) = self.sck.accept()  # returns new socket and self.addr. client 
            print("running server socket =D")
            data = self.conn.recv(1024)   # receive data from client

            if not data: return       # stop if client stopped

            # Separando os valores 1 - publisher de quem enviou a content, 2 - publisher do topic, 3 - content enviada
            matches = bin_to_tuple(data)
            
            for match in matches:
                if match[0] == "out":
                    self.response_out((match[1], match[2], match[3]))
                elif match[0] == "rd":
                    self.response_rd((match[1], match[2], match[3]))

    def response_out(self, tuple):
        (publisher, topic, content) = tuple

        # Se o topic é novo
        if topic not in self.dictionary.keys():
            self.dictionary[topic] = []

        # Adicionando nova content ao topic
        self.dictionary[topic].append((publisher, content))

        # Exibindo na tela as informações da última content recebida
        print("topic", topic, self.dictionary[topic][-1][0], "said:", self.dictionary[topic][-1][1])
        

    def response_rd(self, match):
        publisher = match[0]
        topic = match[1]
        tuples_to_send = []
        if topic in self.dictionary:
            for tpl in self.dictionary[topic]:
				# Pega a primeira mensagem que encontra daquele autor naquele topico
                if tpl[0] == publisher:
                    tuples_to_send.append((tpl[0],topic,tpl[1]))
        
        list_as_bin = list_to_bin(tuples_to_send)
        self.conn.send(list_as_bin)

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
