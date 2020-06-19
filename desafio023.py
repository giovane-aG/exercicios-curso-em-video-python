number = int(input('Digite um número entre 0 e 9999: '))
if int(number) >= 0 and int(number) <= 9999:
    unidade = number // 1 % 10
    dezena = number // 10 %  10
    centena = number // 100 % 10
    milhar = number // 1000 % 10
    print('unidade:{}'.format(unidade))
    print('dezena:{}'.format(dezena))
    print('centena:{}'.format(centena))
    print('milhar:{}'.format(milhar))
else :
    print('Entre 0 e 9999, seu burro')