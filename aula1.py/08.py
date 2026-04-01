import time  
from random import randint
def boas_vindas():
    print("-"*40)
    print(" Bem-vindo ao nosso aplicativo! ��")
    print("-"*40)
time.sleep(2) #Simula uma pausa para rodar o código 

def boas_vindas_personalizado(nome_da_pessoa):
 print("-"*40)
 print(f"Olá, {nome_da_pessoa}! Seja bem-vindo(a)! ��")
 print("-"*40)

# boas_vindas_personalizado('Rafel')

def somar(a, b):
 resultado = a + b
 return resultado
# Para usar o valor, precisamos guardá-lo em uma variável
soma1 = somar(5, 10)
soma2 = somar(100, 50)
print(f'o primeiro sersultado é: {soma1}')
print(f"O segundo resultado é: {soma2}")
# devo usar print uma def com return para imprimir o resultado 
print(somar(28,23))

def gerar_dados(qtd, min_val, max_val):
    """
    Gera uma LISTA de números aleatórios.
    - qtd: quantos números queremos na lista
    - min_val: o valor mínimo (inclusivo)
    - max_val: o valor máximo (inclusivo)
    """
    
    # A estrutura a seguir se chama "List Comprehension". 
    # É um jeito rápido de criar uma lista usando um loop.
    lista_de_dados = [randint(min_val, max_val) for _ in range(qtd)]
    return lista_de_dados
# Testando a função
dados_aleatorios = gerar_dados(5, 1, 100) # Gera 5 números entre 1 e 100
print(f"Dados gerados: {dados_aleatorios}")

