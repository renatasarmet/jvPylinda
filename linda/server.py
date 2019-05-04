import threading
from threading import Thread
from _thread import *
from socket import socket, AF_INET, SOCK_STREAM
from linda.utils import bin_to_tuple, list_to_bin
from time import sleep

class ServerThread(Thread):
    def __init__(self, HOST, PORT):
        Thread.__init__(self)
        self.sck = socket(AF_INET, SOCK_STREAM) 
        self.sck.settimeout(None)
        self.sck.bind((HOST, PORT))  #-
        self.conn = None
        self.addr = None
        self.dictionary = {}
        self.lock = threading.Lock()
    
    def threaded(self,conn):
        while True:
            
            data = conn.recv(1024)   # receive data from client
            if not data: break       # stop if client stopped
            print("Thread: ", threading.get_ident())
            # Separando os valores 1 - publisher de quem enviou a content, 2 - publisher do topic, 3 - content enviada
            matches = bin_to_tuple(data)
            
            for match in matches:
                if match[0] == "out":
                    self.response_out((match[1], match[2], match[3]))
                elif match[0] == "rd":
                    self.response_rd(conn,(match[1], match[2], match[3]))
                elif match[0] == "in":
                    self.response_in(conn,(match[1], match[2], match[3]))

    def run(self):
        while True:
            self.sck.listen(1)
            (self.conn, self.addr) = self.sck.accept()  # returns new socket and self.addr. client 
            print("Client conected.")
            start_new_thread(self.threaded, (self.conn,)) 
            print("Thread created for user")

    def response_out(self, tuple):
        self.lock.acquire()
        (publisher, topic, content) = tuple

        # Se o topic eh novo
        if topic not in self.dictionary.keys():
            self.dictionary[topic] = []

        # Adicionando nova content ao topic
        self.dictionary[topic].append((publisher, content))

        # Exibindo na tela as informacoes da ultima content recebida
        print("topic", topic, self.dictionary[topic][-1][0], "said:", self.dictionary[topic][-1][1])
        self.lock.release()

    def response_rd(self, conn,match):
        self.lock.acquire()
        publisher = match[0]
        topic = match[1]
        tuples_to_send = []
        while(True):
            if topic in self.dictionary:
                for tpl in self.dictionary[topic]:
                    # Pega a primeira mensagem que encontra daquele autor naquele topico
                    if tpl[0] == publisher:
                        tuples_to_send.append((tpl[0],topic,tpl[1]))


            if(len(tuples_to_send) != 0):
                break
            else:
                self.lock.release()
                sleep(5)
                self.lock.acquire()
                
        list_as_bin = list_to_bin(tuples_to_send)
        conn.send(list_as_bin)
        conn.send(".".encode())
        self.lock.release()
    
    def response_in(self, conn,match):
        self.lock.acquire()
        publisher = match[0]
        topic = match[1]
        content = match[2]
        tuples = []
        found = False
        while(not found):
            if topic in self.dictionary:
                vetor = self.dictionary[topic]
                for x in range(len(vetor)):
                    if vetor[x] == (publisher,content):
                        del(vetor[x])
                        print("Deleted message: '{}' from {} at {} ".format(content,publisher,topic))
                        found = True
                        if(len(vetor) == 0):
                            del(self.dictionary[topic])
                        else:
                            self.dictionary[topic]=vetor
                        break
            if(not found):
                self.lock.release()
                sleep(5)
                self.lock.acquire()
        self.lock.release()

    def __del__(self):
        if self.conn:
            self.conn.close()               # close the self.connection
        self.join()


def create_server(HOST=None, PORT=None):
    """
        Faz da maquina que chama essa funcao o servidor
    """
    print(HOST)
    server_thread = ServerThread(HOST=HOST, PORT=PORT)
    server_thread.start()
