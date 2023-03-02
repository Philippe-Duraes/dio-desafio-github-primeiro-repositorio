nome = input('Por favor digite o seu nome: ') 
idade = input('Por favor digite sua idade: ') 

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
   
    if ' ' in nome:
        print(f'Seu nome, {nome} ele contém espaços.')
    else:
        print(f'Seu nome {nome} não contém espaços.')
   
    print(f'Seu nome tem {len(nome)} letras. ')
    print(f'A primeira letra do seu nome é = {nome[0]}')
    print(f'A última letra do seu nome é = {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')