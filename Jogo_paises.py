import random as r
import math
from dados import *

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
def mostra_inventario(dic_dist, dic_dicas):
    print('Distâncias:')
    if dic_dist != {}:
        for pais,d in dic_dist.items():
            print('      '+ str(int(d)) + ' km -> ' + str(pais))
    
    print('')
    print('Dicas:')
    if dic_dicas != {}:
        for tipo,resp in dic_dicas.items():
            print('      -'+ str(tipo) + ': ' + str(resp))

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
for cor in dic_paises[pais]["bandeira"].values():
    l_cor_bandeira.append(cor)

print(l_cor_bandeira)
print(dic_paises[pais]["capital"])

l_lista_capital = []
for letra in dic_paises[pais]["capital"].values():
    l_cor_bandeira.append(cor)

tentativa = 20
lista_tentativas = []
distancias = {}
while tentativa != 0:
    jogada = str(input('Qual o seu palpite? '))
    if jogada == 'desisto':
        certeza = str(input('Tem certeza que você quer desistir? [s/n] '))
        if certeza == 's':
            print('O pais era: {}'.format(pais))
            print('')
            continua = str(input('Quer jogar de novo? [s/n] '))
            if continua == 's':
                tentativa = tentativa
            else:
                print('')
                print('Até a próxima!')
                tentativa = 0
        else:
            print('')
            tentativa = tentativa

    elif jogada == 'dica':
        print('Mercado de dicas')   
        print ('----------------------------------------') 
        print ('1. Cor da bandeira  - custa 4 tentativas')
        print ('2. Letra da capital - custa 3 tentativas')
        print ('3. Área             - custa 6 tentativas')
        print ('4. População        - custa 5 tentativas')
        print ('5. Continente       - custa 7 tentativas')
        print ('0. Sem dica')
        print ('----------------------------------------')
        opcao = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
        if opcao == 0:
            tentativa = tentativa
        #elif opcao = 1:
