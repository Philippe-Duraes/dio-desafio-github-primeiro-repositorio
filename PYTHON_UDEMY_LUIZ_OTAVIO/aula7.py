entrada = input('Por favor digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    if entrada_int % 2 == 0:
        print('Esse número é par !!!.')
    elif entrada_int != 0:
        print('Esse número é ímpar !!!.')
else:
    print('Você não digitou um número inteiro.')
   
   
    



    






