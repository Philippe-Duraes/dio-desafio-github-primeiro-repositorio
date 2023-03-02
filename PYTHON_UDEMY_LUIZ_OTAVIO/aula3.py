nome = 'Philippe Duraes Macedo'
altura = 1.80
peso = 83
imc = peso / (altura ** 2)
resposta = '{0} tem {1:.2f} de altura,pesando {2} quilos e seu IMC é {3:.2f}'

print(resposta.format(nome,altura,peso,imc))
