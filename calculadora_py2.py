saida = ''

def adicao (n1, n2):
    return n1 + n2
def subtracao (n1, n2):
    return n1 - n2
def multiplicacao (n1, n2):
    return n1 * n2
def divisao (n1, n2):
    if n2 == 0:
        return "não foi possível realizar a divisão por 0!"
    else:
        return n1 / n2

def calculadora(n1, n2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        return adicao(n1, n2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        return subtracao(n1, n2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        return multiplicacao(n1, n2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        return divisao(n1, n2)
    
while saida.lower() != 'n':
    n1 = float(input("Digite um número!: "))
    n2 = float(input("Digite outro número!: "))
    operacao = input("Digite a operação!: ")

    resultado = calculadora (n1, n2, operacao)
    print("O Resultado é: ", resultado)

    saida = input("Deseja continuar? (S/N): ")

print("Programa encerrado!")