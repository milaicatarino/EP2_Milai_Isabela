import random as r
import math

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

print ('==========================================')
print ('••••••••••••••••••••••••••••••••••••••••••')
print ("-----Bem-vindo ao Jogo Insper Países!-----")
print ('••••••••••••••••••••••••••••••••••••••••••')
print ('========== Design de Software ============')
print ('')
print ('Possíveis comandos:')
print ('    dica = entra no mercado de dicas')
print ('    desisto = desiste da rodada')
print ('    inventário = exibe sua posição')
print ('')
print ('Um país foi sorteado aleatoriamente, tente adivinhar!')
print ('Você tem 20 tentativa(s)')
print ('')
input('Qual o seu palpite?')