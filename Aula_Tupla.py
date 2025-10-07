import os
os.system('cls')                                            

compras=('arroz','feijão','alho','ovo','leite')
print(compras)

print("="*25)

print(compras[1])

print("="*25)

print(compras[0:2])

print("="*25)

print(len (compras))

print("="*25)

for c in compras:
    print(c)

print("="*25)

for c in range(0,len(compras)):
    print(c)

print("="*25)

for c in range(0,len(compras)):
    print(f'{compras [c]} está na posição {c+1}')

print("="*25)

for item in compras:
    print(f"Eu vou comprar {item}")

print("="*25)

for pos ,item in enumerate (compras):
    print (f"Eu vou comprar {item} na posição {pos+1}")

print("="*25)

a=(2,5,4)
b=(5,8,1,2)
c=a+b
print(c)
print(c.count(4))#Quantos 4
print(c.index(4))#posição do primeiro número 4

print("="*25)