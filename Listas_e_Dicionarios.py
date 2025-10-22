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

print(brasil[1]['uf'])

print("="*65)

materia= dict()
curso=list()

#for c in range(0,3):
   # materia['sigla']=str(input("Digite a Sigla da Matérie:"))
 #   materia['nome']=str(input("Digite o nome da Matéria:"))
 #   curso.append(materia.copy())
#print(curso)

#for m in curso:
#  for k, v ,in m.items():
 #       print(f"O campo {k} tem valor {v}")

#lista=[]
#dic=dict()

#nome=input("Digite:")
#idade=int(input("Digite:"))

#lista.append(nome)
#lista.append(idade)

#dic={"nome":lista[0],"idade":lista[1]}
#print(lista)
#print(dic['nome'])

dados={
    'Crossfox':{'km':35000, 'ano':2005},
    'DS5':{'km':17000,'ano':2015},
    'Fusca':{'km':130000,'ano':1979},
    'Jetta':{'km':56000,'ano':2011},
    'Passat':{'km':62000,'ano':1999},
}

for item in dados.items():
    print(item)
for item in dados.items():
    print(item[1]['ano']) 