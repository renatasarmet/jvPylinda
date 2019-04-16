import re

def bin_to_tuple(binary_data):
    """
        Transforma uma tupla em binário para um objeto (nome, grupo, mensagem)
        :param binary_data: dado em cadeia codificada
        :return: tupla (nome, grupo, mensagem)
    """
    # Definição do padrão da expressão regular
    _pattern = '\(\"([^"]*)\"\,\"([^"]*)\"\,\"([^"]*)\"\)'
    # Separando os valores 1 - nome de quem enviou a mensagem, 2 - nome do grupo, 3 - mensagem enviada
    m = re.findall(_pattern,binary_data.decode())

    return m

def tuple_to_bin(tuple_data):
    """
        Transforma uma tupla de 3 posições para uma cadeia codificada
        :param tuple_data: dado em tupla
        :return: cadeia codificada da tupla
    """
    _msg_send = '("%s","%s","%s")' % (tuple_data[0], tuple_data[1], tuple_data[2])
    return _msg_send.encode()