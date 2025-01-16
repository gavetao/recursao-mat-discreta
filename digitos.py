# Escreva uma função recursiva para calcular a soma dos dígitos de um número inteiro e positivo,
# onde o número é fornecido como parâmetro.
# Por exemplo, a chamada da função para o valor 12345 deve retornar 15.


def somatorio(n):
    if n < 10:
        return n
    return n % 10 + somatorio(n // 10)
