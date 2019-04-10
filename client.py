from socket  import *
from constCS import * #-

if __name__ == "__main__":
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT)) # connect to server (block until accepted)
    nome = str(input("Nome: "))
    grupo = str(input("Grupo: "))
    print("pode começar a falar :D")
    try:
        while True:
            msg = str(input("?: "))
            msg_send = '("%s","%s","%s")' % (nome, grupo, msg)
            s.send(msg_send.encode())  # send some data
            data = s.recv(1024)     # receive the response
            print(data)              # print the result
        s.close()
    except:
        s.close()               # close the connection
