import os
import time
os.system('cls')
# Feito com o fluxograma do Jessé

respostas = 0
while respostas == 0:

    times = ('palmeiras', "flamengo", "cruzeiro", "mirassol", "botafogo", "bahia", "fluminense", "são paulo", "rb bragantino", "ceará", "vasco", "corinthians", "grêmio", "atlético mineiro", "internacional", "santos", "vitória", "fortaleza", "juventude", "sport")
    print(times[0:5])
  
    print("\n",times[16:20])
    
    lista_times = sorted(times)
    times = tuple(lista_times)
    print("\n", times)
    
    print("\n","Corinthians está na posição:",times.index("corinthians") + 1,"°")


    respostas =0
    resposta = str(input("Deseja voltar aos 5 primeiros? s/n: "))

    if resposta == "n":
        respostas = 1
    else: 
        print("Obrigado por usar.")
        respostas = 0