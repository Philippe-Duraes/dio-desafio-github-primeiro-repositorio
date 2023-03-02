horas_atuais = float(input('Digite o horário atual: '))

if 0 <= horas_atuais <= 11:
    print(f'Bom dia já são {horas_atuais:.2f} horas e minutos.')
elif 12 <= horas_atuais <= 17:
    print(f'Boa tarde já são {horas_atuais:.2f} horas e minutos.')
elif 18 <= horas_atuais <= 23:
    print(f'Boa noite já são {horas_atuais:.2f} hora e minutos.')
else:
    print('Você não inseriu dados válidos.')