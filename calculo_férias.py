# Kevin Domingues Braga Calantone 
# Programa que calcula o valor total das férias

print(' _______________________________________________________________________________________')
print('|                 PROGRAMA DE FÉRIAS!                                                   |')
print('| QUANTIDADE MINIMA DE PESSOAS POR APARTEMNTO: 1                                        |')
print('| QUANTIDADE MAXIMA DE PESSOAS POR APARTEMNTO: 6                                        |')
print('|  Quantidade de Pessoas Diária Diária                                                  |')
print('|  no Apartamento tipo 1(R$) tipo2 (R$)                                                 |')
print('|  1 20,00 25,00                                                                        |')
print('|  2 28,00 34,00                                                                        |')
print('|  3 35,00 42,00                                                                        |')
print('|  4 42,00 50,00                                                                        |')
print('|  5 48,00 57,00                                                                        |')
print('|  6 53,00 63,00                                                                        |')
print('|_______________________________________________________________________________________|')
print('\n')

# Entrada de dados
quantidade = int(input('DIGITE A QUANTIDADE DE PESSOAS QUE IRÃO FICAR NO APARTAMENTO: '))
while quantidade < 1 or quantidade > 6:
    print('Quantidade inválida. \n (min: 1| max: 6)')
    quantidade = int(input('DIGITE A QUANTIDADE DE PESSOAS QUE IRÃO FICAR NO APARTAMENTO: '))

apartamento = int(input('INFORME QUAL APARTAMENTO VOCÊ DESEJA (1 OU 2): '))
while apartamento != 1 and apartamento != 2:
    print('Número inválido. (1 ou 2)')
    apartamento = int(input('INFORME QUAL APARTAMENTO VOCÊ DESEJA (1 OU 2): '))

tempo = int(input('QUANTOS DIAS VOCÊ VAI FICAR COM O APARTAMENTO: '))

# Listas de preços
escolha1 = [20.00, 28.00, 35.00, 42.00, 48.00, 53.00]  # Apartamento tipo 1
escolha2 = [25.00, 34.00, 42.00, 50.00, 57.00, 63.00]  # Apartamento tipo 2

# Escolha da diária correta com base na quantidade de pessoas
if apartamento == 1:
    diaria = escolha1[quantidade - 1]  # Índice da lista é quantidade-1
else:
    diaria = escolha2[quantidade - 1]

# Cálculo do valor total
valor_total = diaria * tempo

# Saída: exibição do valor total a pagar
print(f'VALOR A SER PAGO: R$ {valor_total:.2f}')
