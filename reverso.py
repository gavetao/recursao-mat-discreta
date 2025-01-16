# Escreva uma função recursiva retornar um valor inteiro e positivo em ordem reversa,
# onde o valor é fornecido como parâmetro.
# Por exemplo, a chamada da função para o valor 123 deve retornar 321.
# Obs.: Não utilizar um vetor ou string para representar o valor.


def reverso(n, r=0):
    if n == 0:
        return r
    return reverso(n // 10, r * 10 + n % 10)
