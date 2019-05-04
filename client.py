from socket  import *
from constCS import * #-
from linda.utils import tuple_to_bin


# comecando a pensar em um padrao para receber uma lista de tuplas
# comeca a ser algo como isso, mas so reconhece uma tupla dentro da lista.. precisa colocar a separacao por virgulas e n tuplas
# PADRAO:                               \[(\(\"(.*)\"\,\"(.*)\"\,\"(.*)\"\))\]
# EXEMPLO DO QUE ELE RECONHECE:         [("renata","jv","oi pessoal")]


if __name__ == "__main__":
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT)) # connect to server (block until accepted)

    nome = input("Nome: ")
    grupo = input("Grupo: ")
    print("pode começar a falar :D")

    try:
        while True:
            msg = input("?: ")

            # Formando a tupla a enviar em formato string
            msg_send = tuple_to_bin((nome, grupo, msg))

            s.send(msg_send)  # send some data

            data = s.recv(1024)     # receive the response
            print(data)              # print the result

        s.close()
    except:
        s.close()               # close the connection
