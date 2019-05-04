import re

def bin_to_tuple(binary_data, has_op=True):
    """
        Transforma uma tupla em binário para um objeto (nome, grupo, mensagem)
        :param binary_data: dado em cadeia codificada
        :return: tupla (nome, grupo, mensagem)
    """
    # Definição do padrão da expressão regular
    if has_op:
        _pattern = '(out|rd|in)_\(\"([^"]*)\"\,\"([^"]*)\"\,\"([^"]*)\"\)'
    else:
        _pattern = '\(\"([^"]*)\"\,\"([^"]*)\"\,\"([^"]*)\"\)'
    # Separando os valores 1 - nome de quem enviou a mensagem, 2 - nome do grupo, 3 - mensagem enviada
    m = re.findall(_pattern,binary_data.decode())

    return m

def tuple_to_bin(tuple_data, op):
    """
        Transforma uma tupla de 3 posições para uma cadeia codificada
        :param tuple_data: dado em tupla
        :param op: operacao (out|rd|in)
        :return: cadeia codificada da tupla
    """
    _msg_send = '%s_("%s","%s","%s")' % (op, tuple_data[0], tuple_data[1], tuple_data[2])
    return _msg_send.encode()

def list_to_bin(list_data):
    """
    """
    _msg_send = '['
    for tpl in list_data:
        _msg_send += '("%s","%s","%s")' % (tpl[0], tpl[1], tpl[2])
    _msg_send += ']'
    return _msg_send.encode()

def bin_to_list(binary_data):
    """
    """
    pass
