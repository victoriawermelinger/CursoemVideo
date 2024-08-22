# moeda.py

def aumentar(preco=0, taxa=0, formato = False):
    """ -> Calcular o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param: preço: o preço que se quer reajustar
    :param: taxa: qual é a porcentagem do aumento
    :param: formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato = False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preco=0, formato = False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato = False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


