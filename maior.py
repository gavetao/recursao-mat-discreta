# Achar maior elemento de um vetor.


def maior(v, n):
    if n == 1:
        return v[0]
    m = maior(v, n - 1)
    return v[n - 1] if v[n - 1] > m else m
