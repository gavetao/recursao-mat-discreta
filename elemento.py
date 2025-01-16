# Achar um elemento em um vetor ordenado de comprimento potência de 2.


def elemento(e, v, n):
    if n == 1:
        return True if e == v[0] else False
    n //= 2
    if e <= v[n - 1]:
        return elemento(e, v[:n], n)
    if e >= v[n]:
        return elemento(e, v[n:], n)
