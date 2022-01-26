ano = int(input("Digite ano : "))

rest = (ano%4)
div = (ano/100)
rest400 = (ano%400)
    
if rest == 0 and div != 0 or rest400 == 0:
    print('Ano Bissexto')
else:
    print('Ano não Bissexto')



