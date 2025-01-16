# Escreva uma função recursiva para escrever em ordem os valores inteiros de x a y,
# onde x e y são fornecidos como parâmetro.
# Obs.: A lista a ser escrita pode estar em ordem crescente ou decrescente.


def ordenar(x, y, lista=[]):
    if x == y:
        lista.append(x)
        return lista
    if x > y:
        lista.append(x)
        return ordenar(x - 1, y, lista)
    if x < y:
        lista.append(x)
        return ordenar(x + 1, y, lista)
