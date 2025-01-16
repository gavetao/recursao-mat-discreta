# Escreva uma função recursiva para computar a soma de todos os números de 1 a n,
# onde n é fornecido como parâmetro.


def somatorio(n):
    if n == 1:
        return 1
    return n + somatorio(n - 1)
