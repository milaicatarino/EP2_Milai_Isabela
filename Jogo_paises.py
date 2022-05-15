import random as r
import math
from dados_paises import *

# Funções necessárias
# Normalizando bases de países
def normaliza(dic):
    dic2 = {}
    dicad = {}
    for continente in dic:
        dicad["continente"] = continente
        for pais in dic[continente]:
            dic2[pais] = dic[continente][pais] 
            dic2[pais].update(dicad)
    return dic2

# Sorteando países 
def sorteia_pais(dic):
    paises = []
    for pais in dic.keys():
        paises.append(pais)
    pais = r.choice(paises)
    return pais

# Distância
def haversine(r, s_lat, s_lng, e_lat, e_lng):

    s_lat = s_lat*math.pi/180                     
    s_lng = s_lng*math.pi/180
    e_lat = e_lat*math.pi/180                   
    e_lng = e_lng*math.pi/180

    d = 2 * r * math.asin((math.sin((e_lat - s_lat)/2)**2 + math.cos(s_lat)*math.cos(e_lat) * math.sin((e_lng - s_lng)/2)**2)**(1/2))

    return d

# Adicionando em uma lista
def adiciona_em_ordem(pais,dist,l_paises):
    if l_paises == [] or len(l_paises) == 1:
        l_paises.append([pais,dist])
        return l_paises
    for i in l_paises:
        if i[0] == pais:
            return l_paises
    for j in range(0,len(l_paises)):
        if l_paises[j][1] > dist:
            l_paises.insert(j,[pais,dist])
            return l_paises

# Está na lista?
def esta_na_lista(pais, l_paises):
    for i in l_paises:
        if i[0] == pais:
            return True 
    else:
        return False

# Sorteia letra com restrição
def sorteia_letra(palavra,lista):
    p = palavra.lower()
    saida = []
    especial = ['.', ',', '-', ';', ' ']

    for i in range(0,len(p)):
        if p[i] not in lista:
            if p[i] not in especial:
                saida.append(p[i])
              
    return r.choice(saida)

# Mostra inventario
def mostra_inventario(l_dist, dic_dicas, tentativa):
    print('Distâncias:')
    if l_dist != []:
        for lista in l_dist:
            if int(lista[1]) <= 1000:
                print(f'\033[32m      {str(int(lista[1]))} km -> {str(lista[0])}\033[m')
            elif int(lista[1]) <= 2500:
                print(f'\033[33m      {str(int(lista[1]))} km -> {str(lista[0])}\033[m')
            elif int(lista[1]) <= 5000:
                print(f'\033[34m      {str(int(lista[1]))} km -> {str(lista[0])}\033[m')
            elif int(lista[1]) <= 6500:
                print(f'\033[37m      {str(int(lista[1]))} km -> {str(lista[0])}\033[m')
            elif int(lista[1]) <= 8000:
                print(f'\033[35m      {str(int(lista[1]))} km -> {str(lista[0])}\033[m')
            else:
                print(f'\033[31m      {str(int(lista[1]))} km -> {str(lista[0])}\033[m')
    
    print('')
    print('Dicas:')
    if dic_dicas != {}:
        for tipo,resp in dic_dicas.items():
            print('      -'+ str(tipo) + ': ' + str(resp))
    
    print('')
    print('Você tem {} tentativa(s).'.format(tentativa))
    return ' '

# Mosta dicas
def mostra_dicas(l_dica_disponivel,tentativa):
    print('Mercado de dicas')   
    print ('----------------------------------------') 
    if 1 in l_dica_disponivel and tentativa >= 4:
        print ('1. Cor da bandeira  - custa 4 tentativas')
    if 2 in l_dica_disponivel and tentativa >= 3:
        print ('2. Letra da capital - custa 3 tentativas')
    if 3 in l_dica_disponivel and tentativa >= 6:
        print ('3. Área             - custa 6 tentativas')
    if 4 in l_dica_disponivel and tentativa >= 5:
        print ('4. População        - custa 5 tentativas')
    if 5 in l_dica_disponivel and tentativa >= 7:
        print ('5. Continente       - custa 7 tentativas')
    print ('0. Sem dica')
    print ('----------------------------------------')

# Cria lista das dicas disponiveis
def dicas_possiveis(tentativa):
    if tentativa <= 2:
        for num in l_dica_disponivel:
            if num != 0:
                indice = l_dica_disponivel.index(num)
                del l_dica_disponivel[indice]
    elif tentativa <= 3:
        for num in l_dica_disponivel:
            if num != 0 and num != 2:
                indice = l_dica_disponivel.index(num)
                del l_dica_disponivel[indice]
    elif tentativa <= 4:
        for num in l_dica_disponivel:
            if num != 0 and num != 2 and num != 1:
                indice = l_dica_disponivel.index(num)
                del l_dica_disponivel[indice]
    elif tentativa <= 5:
        for num in l_dica_disponivel:
            if num != 0 and num != 2 and num != 1 and num != 4:
                indice = l_dica_disponivel.index(num)
                del l_dica_disponivel[indice]
    elif tentativa <= 6:
        for num in l_dica_disponivel:
            if num != 0 and num != 2 and num != 1 and num != 4 and num != 3:
                indice = l_dica_disponivel.index(num)
                del l_dica_disponivel[indice]

    return l_dica_disponivel

# Calcular distancias
def calcula_distancia(jogada, pais):
    for p in dic_paises:
        if p == jogada:
            lat = dic_paises[p]["geo"]["latitude"]
            long = dic_paises[p]["geo"]["longitude"]
        elif p == pais:
            lat_pais = dic_paises[p]["geo"]["latitude"]
            long_pais = dic_paises[p]["geo"]["longitude"]
    r = 6371
    return haversine(r, lat, long, lat_pais, long_pais)

print ('==========================================')
print ('••••••••••••••••••••••••••••••••••••••••••')
print ("-----Bem-vindo ao Jogo Insper Países!-----")
print ('••••••••••••••••••••••••••••••••••••••••••')
print ('========== Design de Software ============')
print('')
print ('Possíveis comandos:')
print ('    dica = entra no mercado de dicas')
print ('    desisto = desiste da rodada')
print ('    inventário = exibe sua posição')
print('')
dic_paises = normaliza(dic)
pais = sorteia_pais(dic_paises)
print ('Um país foi sorteado aleatoriamente, tente adivinhar!')
print ('Você tem 20 tentativa(s)')

l_cor_bandeira = []
for cor,porcentagem in dic_paises[pais]["bandeira"].items():
    if porcentagem != 0 and cor != 'outras':
        l_cor_bandeira.append(cor)

l_capital_escolhida = []

area_pais = dic_paises[pais]["area"]

populacao = dic_paises[pais]["populacao"]

continente = dic_paises[pais]["continente"]

tentativa = 20
l_paises = []
for pais in dic_paises.keys():
    l_paises.append([pais,dic_paises[pais]["area"]])
l_dist = []
dic_dicas = {}
l_cores = []
l_cap = []
l_dica_disponivel = [0,1,2,3,4,5]
l_palpites = []

while tentativa >= 0:
    if tentativa != 0:
        jogada = str(input('Qual o seu palpite? '))
        if jogada == 'desisto':
            certeza = str(input('Tem certeza que você quer desistir? [s/n] '))
            if certeza == 's':
                print('O país era: {}'.format(pais))
                print('')
                continua = str(input('Quer jogar de novo? [s/n] '))
                if continua == 's':
                    tentativa = tentativa
                else:
                    print('')
                    print('Até a próxima!')
                    tentativa = -1
            else:
                print('')
                tentativa = tentativa

        elif jogada == 'dica':
            print(mostra_dicas(l_dica_disponivel,tentativa))
            opcao = int(input('Escolha sua opção {}: '.format(dicas_possiveis(tentativa))))  
            if opcao == 0:
                tentativa = tentativa
            elif opcao == 1:
                cor_dica = r.choice(l_cor_bandeira)
                l_cores.append(cor_dica)
                dic_dicas['Cor da bandeira'] = l_cores
                indice = l_cor_bandeira.index(cor_dica)
                del l_cor_bandeira[indice]
                tentativa -= 4
                print(mostra_inventario(l_dist, dic_dicas, tentativa))
            elif opcao == 2:
                cap_dica = sorteia_letra(dic_paises[pais]["capital"],l_capital_escolhida)
                l_cap.append(cap_dica)
                dic_dicas['Letra da capital'] = l_cap
                l_capital_escolhida.append(cap_dica)
                tentativa -= 3
                print(mostra_inventario(l_dist, dic_dicas, tentativa))
            elif opcao == 3:
                dic_dicas['Área (km2)'] = area_pais
                tentativa -= 6
                print(mostra_inventario(l_dist, dic_dicas, tentativa))
                indice = l_dica_disponivel.index(3)
                del l_dica_disponivel[indice]
            elif opcao == 4:
                dic_dicas['População'] = populacao
                tentativa -= 5
                print(mostra_inventario(l_dist, dic_dicas, tentativa))
                indice = l_dica_disponivel.index(4)
                del l_dica_disponivel[indice]
            elif opcao == 5:
                dic_dicas['Continente'] = continente
                tentativa -= 7
                print(mostra_inventario(l_dist, dic_dicas, tentativa))
                indice = l_dica_disponivel.index(5)
                del l_dica_disponivel[indice]
        
        elif jogada == "inventario":
            print(mostra_inventario(l_dist, dic_dicas, tentativa))
            tentativa = tentativa

        elif jogada == pais:
            print(f'\033[36mParabénsssss!! Você ganhou o jogo.\033[m')
            tentativa = 0

        else:
            if esta_na_lista(jogada, l_paises):
                if not esta_na_lista(jogada, l_palpites):
                    distancia = calcula_distancia(jogada, pais)
                    l_dist = adiciona_em_ordem(jogada,distancia,l_dist)
                    tentativa -= 1
                    print(mostra_inventario(l_dist, dic_dicas, tentativa))
                    l_palpites.append(jogada)
            else:
                print('Não reconheço esse país. Tente novamente.')
                tentativa = tentativa 
                print ('')
                
    else:
        print('Você perdeu =(')
        print('O país era: {}'.format(pais))
        continua = str(input('Quer jogar de novo? [s/n] '))
        if continua == 's':
            print('')
            tentativa = 20
        else:
            print('')
            print('Até a próxima!')
            tentativa = -1
