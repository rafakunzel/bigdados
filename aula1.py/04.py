# for i in range(5):
#     try:
#  # i representa o número atual da repetição (0, 1, 2...)
#         print(f"Número {i + 1} de 5:")
#         num = float(input("Digite um número: "))
#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4
#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
 
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")
# print("--- Usando WHILE (Repetição Condicional) ---")
# contador = 0 # Inicializamos o contador
# limite = 5 # Definimos o limite
# while contador < limite: # A condição de parada: Enquanto o contador for menor que 5
#  try:
#  print(f"Número {contador + 1} de {limite}:")
#  num = float(input("Digite um número: "))
 
#  dobro = num * 2
#  triplo = num * 3
#  quádruplo = num * 4
 
#  print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
 
#  contador = contador + 1 # IMPORTANTÍSSIMO! Incrementa o contador para evitar loop
# infinito
 
#  except ValueError:
#  print("Entrada inválida. Tente novamente.")
#  # Não incrementamos o contador para dar nova chance ao usuário
somanot=0
for i in range(10):
    print(f"Número {i + 1} de 10:")
    notas = float(input("Digite a nota da prova:"))
    somanot+=notas
print(somanot)
med=somanot/10
print(med)
if med>6:
    print('aprovado')
elif med>= 3 and med<6:
    print('recuperação')
else:
    print('rerpovado')




