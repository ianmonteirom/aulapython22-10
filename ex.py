from random import randint


def busca_linear(lista, item):
    for i in range(len(lista)):         # percorre lista do índice 0 a n–1
        if lista[i] == item:
            return i                    # encontrou item na posição de índice i
    return -1                           # não encontrou o item


def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2      # índice da metade da lista
        if lista[meio] == item:         # encontrou item
            return meio
        elif item > lista[meio]:        # busca na segunda metade da lista
            inicio = meio + 1
        else:                           # busca na primeira metade da lista
            fim = meio - 1
    return -1                           # não encontrou o item


def busca_binaria_alteracao(lista, item, novo_valor):
    """
    EXERCÍCIO 1:
    Implemente a função 'busca_binaria_alteracao', alterando o algoritmo de
    busca binária para que ele se torne um algoritmo de atualização.
    Caso seja encontrado o item, ele faz a alteração para um novo valor.
    Deve alterar apenas a primeira ocorrência do valor encontrado.
    """

    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            print(lista[meio])
            lista[meio] = novo_valor
            print(lista[meio])
            return meio
        elif item > lista[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


def busca_linear_comparacoes(lista, item):
    """
    EXERCÍCIO 2:
    Implemente a função 'busca_linear_comparacoes', alterando o algoritmo de
    busca linear para que a função retorne a quantidade de comparações realizadas
    na tentativa de encontrar um determinado item.
    """
    pass



def busca_binaria_comparacoes(lista, item):
    """
    EXERCÍCIO 3:
    Implemente a função 'busca_binaria_comparacoes', alterando o algoritmo de
    busca binária para que a função retorne a quantidade de comparações realizadas
    na tentativa de encontrar um determinado item.
    """
    pass


def busca_binaria_recursiva(lista, item, inicio, fim):
    """
    EXERCICÍO 4
    Implemente uma versão recursiva da função de busca binária.
    """
    pass


# lista = [randint(1, 100) for _ in range(100)]

lista = [20, 23, 40, 45, 50, 100, 76]

print(lista)
busca_binaria_alteracao(lista, 23, 220)
print(lista)
