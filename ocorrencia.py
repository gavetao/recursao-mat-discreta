# Escreva uma função recursiva para contar quantas vezes o caractere c ocorre na string s,
# onde o caractere e a string são fornecidos como parâmetro.


def ocorrencia(c, s):
    if s == "":
        return 0
    if s[0] == c:
        return 1 + ocorrencia(c, s[1:])
    return ocorrencia(c, s[1:])
