while  True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite um operador entre +-/*: ')

    numeros_validos = None
    operador_valido = '+-/*'

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:    
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos')
        continue    
     
    if operador not in operador_valido:
        print('O operador digitado é inválido.')    
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.') 
        continue

    if operador == '+':
        soma = num1_float + num2_float
        print(f'A soma dos números é {soma}')
    
    if operador == '-':
        subtracao = num1_float - num2_float
        print(f'A subtracao dos números é {subtracao}')        
    
    if operador == '*':
        multiplicacao = num1_float * num2_float
        print(f'A multiplicação dos números é {multiplicacao}')
    
    if operador == '/':
        divisao = num1_float / num2_float
        print(f'A divisao dos números é {divisao}')

    sair = input('Digite [s]im para sair: ').lower().startswith('s')

    if sair is True:
        break

print('O programa foi encerrado.')

