pessoas=[ ["João",10], ["Pedro",15], ["José",18] ]
print(pessoas[1][0])

print("="*30)

print(pessoas[2])

print("="*30)

teste=list()
teste.append('Rodrigo')
teste.append(25)
print(teste)

print("="*30)

galera=list()
galera.append(teste[:])#Lista individual
print(galera)

print("="*30)

teste[0]='Maria'
teste[1]=22
galera.append(teste[:])#Lista individual
print(teste)

print("="*30)

turma=[['ana',15],['João',20],['Pedro',22],['Raul',44]]
print(turma)
print(turma[0])
print(turma[1][1])

print("="*30)

turma=[['Ana',15],['João',20],['Pedro',22],['Raul',44]]
for p in turma:
    print(p)

print("="*30)

for p in turma:
    print(p[0])

print("="*30)

for p in turma:
    print(p[1])

print("="*30)

for p in turma:
    print(f"{p[0]} tem {p[1]} anos de idade")

print("="*30)

turma2=list()
dados=list()

for c in range(0,6):
    dados.append((str(input("Nome: "))) .upper() .strip())
    dados.append(int(input("Idade: ")))
    turma2.append(dados[:])
    dados.clear()
print(turma2)

turma2=list()
dados=list()
totmaior = totmenor = 0

for c in range(0,6):
    dados.append((str(input("Nome: "))) .upper() .strip())
    dados.append(int(input("Idade: ")))
    turma2.append(dados[:])
    dados.clear()

for p in turma2:
    if p[1]>= 18:
        print(f"{p[0]} é maio de idade, ele tem {p[1]} anos de idade")
        totmaior +=1
    else:
        print(f"{p[0]} é menor de idade , ele tem {p[1]} anos de idade")
        totmenor +=1
        
print("="*30)
print(f"Temos {totmaior} maiores de idade e {totmenor} menores de idade")