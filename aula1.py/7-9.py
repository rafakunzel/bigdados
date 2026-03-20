#coleta de dados
dadosentra=[]
print('digite 5 anos de filmes:')
for i in range(5):  #para i repita 5 vezes alguma coisa 
    nomes=input(f'filmes {i+1}:')
    dadosentra.append(nomes)
print(dadosentra)

#lista
listafilmes=dadosentra
#tuppla
tuplafilmes=tuple(dadosentra)
print(tuplafilmes)
#set
setfilmes=set(dadosentra)
print(setfilmes)

dicionariofilmes={}
for i in range(len(dadosentra)):
    dicionariofilmes[i+1]=dadosentra[i]
