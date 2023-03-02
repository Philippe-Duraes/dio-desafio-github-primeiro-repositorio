idade = input('Digite sua idade: ')

try:
    idade.isdigit()
    idade_int = int(idade)
    if idade_int >= 18:
        print('Então você é maior de idade.')
    else:
        print('Você é menor de idade')
except:
    print('Você inseriu um dado inválido.')