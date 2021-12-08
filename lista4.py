#Lista4: uso do IF
    
#1 hipotenusa positiva
cat1 = float ( input (' Informe o valor do cateto 1: ') )
cat2 = float ( input (' Informe o valor do cateto 2: ') )
hipotenusa = ((cat1**2)+ (cat2**2)) ** (1/2)
if cat1 <0 or cat2 <0:
    print('os valores são negativos')
if cat1 >0 and cat2 >0:
    print(f'A hipotenusa é: {hipotenusa:.2f}')
    
#2 maior valor
num1 = float ( input ('insira um numero: ') )
num2 = float ( input ('insira outro numero: ') )
if num1 > num2:
    print(f' O maior valor é o {num1}')
if num1 < num2:
    print(f' O maior valor é o {num2}')
    
#3 valor entre 0 e 1
num1 = float ( input ('insira um numero: ') )
if num1 > 0 and num1 < 1:
    print('O valor está entre 0 e 1')
else:
    print('O valor não está entre 0 e 1')

#4 é uma vogal?
let = input ('insira uma letra: ')
if let == 'a' or 'e' or 'i' or 'o' or 'u':
    print ('é uma vogal')
else:
    print('não e uma vogal')

#4 variação vogal
let = input ('insira uma letra: ')
if let == 'a' =='e' =='i' =='o' =='u':
    print ('é uma vogal')
else:
    print('não e uma vogal')
#5 múltiplos
num1 = float ( input ('insira um numero: ') )
num2 = float ( input ('insira outro numero: ') )
if num2 % num1 == 0:
    print(f'{num2} é múltiplo de {num1}')
else:
    print('não são múltiplos')

#6
compra = float ( input ( 'digite o valor da compra: ') )
if compra >= 6900:
    desconto = compra * (0.15)
else:
    desconto = compra * (0.05)
print (f' O desconto é de {desconto:.2f} reais e o valor final é {compra-desconto:.2f} reais')
