# #atividades 
# 1. Cálculo de Lâmpadas:
# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada.

# 2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²

# 3. Rendimento do Taxista:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.

#atividade 4 #refazer com match case 
# cod=int(input('Digite um valor para o código:'))
# if cod==1:
#     print('Sul')
# elif cod==2:
#     print('Norte')
# elif cod==3:
#     print('Leste')
# elif cod==4:
#     print('Oeste')
# elif cod==5 or 6:
#     print('Nordeste')
# elif cod==7 and 8 or 9:
#     print('Sudeste')
# elif cod==10:
#     print('Centro-Oeste')
# elif cod==11:
#     print('Noroeste')
# else:
#     print('Importado')

# #Atvidade5
# avaliação optativa depois da média 
not1=int(input('Digite a nota da prova 1:'))
print(not1)
not2=int(input('Digite a nota da prova 2:'))
print(not2)
med=(not1+not2)/2
if med>6:
    print('aprovado')
elif med>= 3 and med<6:
    print('recuperação')
else:
    print('rerpovado')
opta=float(input('Digite a nota da optativa (ou -1 se não fez): '))
if opta>0:
    if not1>not2:
        #not2=opta
        novmed=(not1+opta)/2
        print(novmed)
    else:
        novmed=(not2+opta)/2
        print(novmed)
    if novmed>6:
        print('aprovado')
    elif novmed>= 3 and med<6:
        print('recuperação')
    else:
        print('rerpovado')
else:
    print(-1)     
# #atividade 6 
# valor=int(input('Digite um valor:'))
# if valor>0:
#     print('positivo')
# else:
#     print('negativo')

#aula:
# try:
#     numero_mes = int(input("Digite um número de 1 a 12: "))
#     match numero_mes:
#         case 1:
#          print("O número 1 corresponde a Janeiro.") 

#         case 12:
#          print("O número 12 corresponde a Dezembro.")
#         case _:
#             print(f"Número {numero_mes} inválido. Digite entre 1 e 12.")
# except ValueError:
#  print("Entrada inválida. Por favor, digite um número inteiro.")
