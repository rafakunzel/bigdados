num=[1,4,7,8,9,5,2,3,6]
#append=adiona elementos no final da lista 
#clear=zera a lista
#copy=copiar a lista
#count=contas quantos elementos tem na lista 
#extend=fundir duas listas 
#index=Encontrar a posição de um item.
#insert=(o que eu quero adicionar,posição) #Adiciona um elemento em uma posição específica
#pop=remove no final da lista
#remove=Remove a primeira ocorrência de um valor específico remove()
#reverse=Inverte a ordem atual dos elementos (o que está no fim vai para o começo), sem necessariamente ordenar.
#sort=organiza a lista na cordem crescente 
#_add_ = 

#Dica importante fazer as alteração na copy ou salvar a lista principal 
#Posso fazer direto na lista num. e os #s ou criar uma variavél: apend=num.append()

## TUPLAS ###
pares=(40,20,2,18,14,34,96,30,20,58)
# iguais na lista 
# print(pares[3])
# print(pares[3:])
# print(pares[3:8])
# print(len(pares)) 
# adiciona elemento no final da tuppla 
# pares=pares+(44,)
#comandos tuppla 
# count 
# index
# lista_pares=list(pares)
# print(lista_pares)
# lista_pares.append(102)
# lista_pares.sort()
# lista_pares=tuple(lista_pares)
# print(lista_pares)

### SETS ###
impares={33,5,17,11,27,11,71,79,99,15}
print(impares)
print(type(impares))
impares_02={11,3,23,83,15,73}
intersecao=impares.intersection(impares_02)
print(intersecao)

### DICIONÁRIOS ###
filme={
    'nome':'V for Vendetta',
    'ano': 2005,
    'genero':'Ação', #Thriller/Drama
    'faixa_etaria':16
}
print(filme)
print(type(filme))

print(filme.keys())
print(filme.values())
print(len(filme))

filme['duracao']='130min'
filme['genero']='Thriller/Drama'
filme['genero']=None
print(filme)
#keys= chaves 
#values= valores 



