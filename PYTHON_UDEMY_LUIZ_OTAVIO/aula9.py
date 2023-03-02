nome = input('Digite seu nome por favor: ')

if len(nome) <= 4:
    print('Seu nome é curto!')
elif 4 < len(nome) <= 6:
    print('Seu nome é normal!')
elif len(nome) > 6:
    print('Seu nome é muito grande!')
