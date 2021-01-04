import matplotlib.pyplot as plt
from math import sqrt
import random
from itertools import permutations

def min(a):
    valor = 100000
    indice = 0
    for i in range(len(a)):
        if a[i] < valor:
            valor = a[i]
            indice = i
    return valor, indice

def suma_valores_lista(a):
    suma = 0
    for i in a:
        suma += i
    return suma

def ditancia_entre_puntos(p1, p2):
    return sqrt(pow(p2[0]- p1[0], 2)+pow(p2[1]- p1[1], 2))

def recorrido_por_distancias_cercanas(coord):
    coordenadas = list(coord)
    indice_actual = 1
    distancias_menores = []
    for a in range(len(coord)):
        distancias = []
        
        for j in range(a + 1, len(coord)):
            distancias.append(ditancia_entre_puntos(coordenadas[a], coordenadas[j]))
        valor, indice = min(distancias)
        distancias_menores.append(valor)
        indice = a+1 + indice
        try:
            v_min = coordenadas[indice]
            coordenadas.pop(indice)
        except IndexError: 
            pass
        
        coordenadas.insert(a+1, v_min)
    coordenadas.pop(len(coordenadas)-1)
    distancias_menores.pop(len(distancias_menores)-1)
    distancias_menores = suma_valores_lista(distancias_menores)
    x = []
    y = []
    for i in coordenadas:
        x.append(i[0])
        y.append(i[1])
    return x,y, distancias_menores

def recorrido_por_menor_distancia(coord):
    tuplas_coordenadas = []
    for i in coord:
        tuplas_coordenadas.append(tuple(i))
    tuplas_coordenadas.pop(0) #elimino el primer elemento para que empiezen en el mismo punto
    coordenadas = set()
    for perm in permutations(tuplas_coordenadas):
        coordenadas.add(perm)

    coordenadas = list(coordenadas) #todas las posibles combinaciones de las coordenadas

    coordenadas_con_primer = []
    for i in coordenadas:
        a = list(i)
        a.insert(0, tuple(coord[0]))
        coordenadas_con_primer.append(a)
    coordenadas = coordenadas_con_primer
    
    distancias = []
    x = []
    y = []
    for i in range(len(coordenadas)):
        distancia = 0
        for j in range(len(coordenadas[i])):
            if j < len(coordenadas[i]) - 1:
                distancia += ditancia_entre_puntos(coordenadas[i][j], coordenadas[i][j + 1])
        distancias.append(distancia)

    distancia_minima, indice = min(distancias)
    for i in coordenadas[indice]:
        x.append(i[0])
        y.append(i[1])
    return x,y,distancia_minima

n = int(input("Cantidad de puntos: "))

x = [random.randint(1, 20) for i in range(n)]
y = [random.randint(1, 20) for i in range(n)]
coordenadas = [] 
for i in range(len(x)):
    coordenadas.append([x[i], y[i]])


x2,y2,d = recorrido_por_menor_distancia(coordenadas)
x1,y1, distancias = recorrido_por_distancias_cercanas(coordenadas)

fig = plt.figure(figsize=(15,15))
fig.tight_layout()
ax = plt.subplot(1,2,1)
plt.plot(x, y, 'o', markersize=5, color="red") #puntos
plt.plot(x1[0], y1[0], 'o', markersize=6, color="blue")#primer punto
plt.plot(x1, y1, markersize=2, color="green")
ax.set_title("metodo por distancia cercana = {}".format(distancias))

ax = plt.subplot(1,2,2)
plt.plot(x, y, 'o', markersize=5, color="red") #puntos
plt.plot(x2[0], y2[0], 'o', markersize=6, color="blue")#primer punto
plt.plot(x2, y2, markersize=2, color="green")
ax.set_title("metodo por menor distancia = {}".format(d))
plt.show()
'''
plt.title("metodo por distancia cercana = {}".format(distancias))
plt.grid()
plt.plot(x, y, 'o', markersize=5, color="red") #puntos
plt.plot(x1[0], y1[0], 'o', markersize=6, color="blue")#primer punto
plt.plot(x1, y1, markersize=2, color="green")
plt.show()

plt.title("metodo por menor distancia = {}".format(d))
plt.grid()
plt.plot(x, y, 'o', markersize=5, color="red") #puntos
plt.plot(x2[0], y2[0], 'o', markersize=6, color="blue")#primer punto
plt.plot(x2, y2, markersize=2, color="green")
plt.show()
'''