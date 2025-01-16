# Escreva uma função recursiva para determinar se um vetor de inteiro é um palíndromo,
# onde o vetor e seu tamanho são fornecidos como parâmetro.


def palindromo(v, n):
    if n <= 1:
        return True
    if v[0] == v[n - 1]:
        return palindromo(v[1:-1], n - 2)
    return False
