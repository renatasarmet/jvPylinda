#-*- coding: utf-8 -*-
from . import utils
from socket  import *
from constCS import * #-
import atexit


s = socket(AF_INET, SOCK_STREAM)

def connect():
	"""
		Começa o servidor
	"""
	s.connect((HOST, PORT)) # connect to server (block until accepted)
	print("conected")
	atexit.register(exit_handler)
	pass

def exit_handler():
    print("desconected")
    s.close()

def __del__():
	"""
		Encerra o servidor
	"""
	print("desconected")
	s.close()


class TupleSpace:

	# Marcar ate qual mensagem a pessoa X leu
	# Interagir com a tuplespace (chamar os metodos dela)

	def __init__(self, **kwargs):
		if kwargs and len(kwargs) == 1 and "blog_name" in kwargs:
			#parametros corretos
			self.blog_name = kwargs["blog_name"]
		else:
			self.blog_name = ""

		self.dictionary = {}


	def _rd(self, t):
		"""
			:param publisher: nome do cliente que publicou a mensagem que sera lida
			:param topic: nome do grupo do qual quer ler a mensagem
			:param type_return: tipo da mensagem a ser lida
			:return:
		"""
		publisher, topic, type_return = t
		print("\nReading messages from {} at {}".format(publisher, topic))

		# Formando a tupla a enviar em formato string
		msg_send = utils.tuple_to_bin((publisher, topic, type_return), "rd")
		s.send(msg_send)
		tuple_list_bin = b''
		r = b''
		while r.decode() != "." :
			tuple_list_bin+=r
			r = s.recv(1)
		tuple_list = utils.bin_to_tuple(tuple_list_bin, has_op=False)
		if tuple_list:
			messages = ""
			for tpl in tuple_list:
				messages += "topic " + tpl[1] + " " + tpl[0] + " said: " + tpl[2] + "\n"

			return messages
		else:
			return publisher + " didn't published in this topic or " + topic + " doesn't exist"
    
	def _in(self, t):
		"""
			:param publisher: nome do cliente que publicou a mensagem que sera apagada
			:param topic: nome do grupo do qual quer apagar a mensagem
			:param type_return: mensagem a ser apagada
			:return:
		"""
		publisher, topic, content = t
		print("\nDeleting message '{}' from {} at {}".format(content, publisher, topic))
		# Formando a tupla a enviar em formato string
		msg_send = utils.tuple_to_bin((publisher, topic, content), "in")
		s.send(msg_send)

	def _out(self, t):
		"""
			:param publisher: nome do cliente que envia a mensagem
			:param topic: nome do grupo para qual envia a mensagem
			:param content: mensagem 
			:return:
		"""
		publisher, topic, content = t
		print("\nWriting message '{}' from {} at {}".format(content, publisher, topic))

		# Exibindo na tela as informações da última mensagem recebida
		# print("grupo", topic, self.dictionary[topic][-1][0], "disse:", self.dictionary[topic][-1][1])

		# Formando a tupla a enviar em formato string
		msg_send = utils.tuple_to_bin((publisher, topic, content), "out")
		s.send(msg_send)  # send some data


	def set_name(self, new_name):
		if new_name or new_name is not None:
			self.blog_name = new_name

class Universe():
	def __init__(self):
		pass
	
	def _rd(self, t):
		"""
			:return: lista/tupla (?) que contem um blog
		"""
		blog_name, tuplespace_class = t

		if tuplespace_class == TupleSpace:
			tuplespace = tuplespace_class(blog_name=blog_name)

		return "", tuplespace

	def _out(self, t):
		blog_name, tuplespace = t
		tuplespace.set_name(blog_name)
		pass

# Universo
universe = Universe()
