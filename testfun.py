def mensage(msg, age):
    print('=' * 20 )
    print('Bem-Vindo {}'.format(msg))
    print('=' * 20 )
    print('Sua idade é {}'.format(age))
    print('=' * 20 )
    

# Programa principal

nome =  str(input('Informe seu nome: '))
idade = int(input('Informe sua idade: '))
mensage(nome, idade)

