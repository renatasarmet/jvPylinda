#-*- coding: utf-8 -*-
from . import utils

def connect():
	"""
		Começa o servidor
	"""
	print("conectado")
	pass

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


	def _rd(self, publisher, topic, type_return):
		pass

	def _out(self, t):
		"""
			:param publisher: nome do cliente que envia a mensagem
			:param topic: nome do grupo para qual envia a mensagem
			:param content: mensagem
			:return:
		"""
		publisher, topic, content = t

		# Se o grupo é novo
		if topic not in self.dictionary:
			self.dictionary[topic] = []

		# Adicionando nova mensagem ao grupo
		self.dictionary[topic].append((publisher, content))


		# Exibindo na tela as informações da última mensagem recebida
		print("grupo", topic, self.dictionary[topic][-1][0], "disse:", self.dictionary[topic][-1][1])

		pass

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
