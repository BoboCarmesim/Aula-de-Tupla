lista=dict() #isso cria um dicionário vazio
lista={'nome':'Pedro','Idade':25}
print(lista['nome'])
print(lista['Idade'])
print(f"{lista['nome']} sua idade é de {lista['Idade']} anos")

print("="*65)

lista['sexo']='M'
print(lista)

print("="*65)

del lista['Idade']
print(lista)

print("="*65)

filme=dict()
filme={'titulo':'StarWars',
       'ano':1977,
       'diretor':'George Lucas'}
print(filme)

print("="*65)

print(filme.values())
print(filme.keys())
print(filme.items())

print("="*65)

for k,v in filme.items():
    print(f"O {k} é {v}")

print("="*65)

pessoas=dict()
pessoas={'nome':'Asdrubal','idade':19,'Sexo':'F'}
#print(pessoas[0])# da ERRO

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")

pessoas['nome']='Leandro'
pessoas['peso']=95
for k,v in pessoas.items():
    print(f"{k} = {v}")

print("="*65)

brasil=[]
estado={'uf':'Rio de Janeiro','sigla':'RJ'}
estado2={'uf':'São Paulo','sigla':'SP'}

brasil.append(estado)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])

print(brasil[1]['sigla'])