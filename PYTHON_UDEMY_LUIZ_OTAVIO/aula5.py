entrada = input('[E]ntrar ou [S]air: ')
senha_permitida = '123456'

if entrada == 'E':
    senha_digitada = input('Senha: ')
    if senha_digitada == senha_permitida:
        print('Você acabou de acessar sua conta.')
else:
    print('Acabamos de encerrar a sua sessão.')


    