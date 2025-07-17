# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n")

print('Selecione o numero da operação: \n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

while True:

    operador = int(input('Digite sua opção (1/2/3/4): '))
    if operador in [1, 2, 3, 4]:
        break
    else:
        print('Valor invalido!')

primeiroNum = float(input('Digite o primeiro numero: '))
segundoNum = float(input('Digite o segundo numero: '))


if operador == 1:
    resultadoSoma = primeiroNum + segundoNum
    print(f'{primeiroNum} + {segundoNum} = {resultadoSoma:.2f}')

elif operador == 2:
    resultadoSub = primeiroNum - segundoNum
    print(f'{primeiroNum} - {segundoNum} = {resultadoSub:.2f}')

elif operador == 3:
    resultadoMulti = primeiroNum * segundoNum
    print(f'{primeiroNum} * {segundoNum} = {resultadoMulti:.2f}')

elif operador == 4:
    resultadoDiv = primeiroNum / segundoNum
    print(f'{primeiroNum} / {segundoNum} = {resultadoDiv:.2f}')

else:
    pass
