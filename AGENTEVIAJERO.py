from heapq import heappop,heappush
from copy import deepcopy
import random

import time
def permutation(lst):
    if len(lst)==0:
        return[]
    if len(lst)==1:
        return[lst]
    l=[]#empty list that will store current permutation
    for i in range(len(lst)):
        m=lst[i]
        remlst=lst[:i]+lst[i+1:]
        for p in permutation(remlst):
            l.append([m]+p)
    return l


class Fila:
    def __init__(self):
        self.fila=[]
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Pila:
    def __init__(self):
        self.pila=[]
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)



def flatten(L):
    while len(L)>0:
        yield L[0]
        L=L[1]

class Grafo:
 
    def __init__(self):
        self.V = set()#un conjunto
        self.E = dict()#un mapeo de pesos de aristas
        self.vecinos = dict()#un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos:#vecindad de v
            self.vecinos[v] = set()#inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso#en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)

      
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def BFS(self,ni):
        visitados=[]
        f=Fila()
        f.meter(ni)
        while (f.longitud>0):
            na=f.obtener()
            visitados.append(na)
            ln=self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados

    def DFS(self,ni):
        visitados=[]
        f=Pila()
        f.meter(ni)
        while (f.longitud>0):
            na=f.obtener()
            visitados.append(na)
            ln=self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados





    def shortests(self,v):#algoritmo de dijkstra
        q=[(0,v,())]#arreglo q de las tuplas de lo que se va a almacenar donde 0 es la distancia, v el nodo y() el camino hacia el
        dist=dict()#diccionario de distancias
        visited=set()#conjunto de visitados
        while len(q)>0:#mientras exista un nodo pendiente
            (l,u,p)=heappop(q)#se toma la tupla con la distancia menor
            if u not in visited:#si no lo hemos visitado
                visited.add(u)#se agrega a visitados
                dist[u]=(l,u,list(flatten(p))[::-1]+[u])#agrega el diccionario
            p=(u,p)#tupla del nodo y el camino
            for n in self.vecinos[u]:#para cada hijo del nodo actual
                if n not in visited:#si no lo hemos visitado
                    el=self.E[(u,n)]#se toma la distancia del nodo actual mas la distancia hacia el nodo hijo
                    heappush(q,(l+el,n,p))#se agrega el arreglo q la distancia actual mas la distancia hacia el nodo hijo n hacia donde se va y el camino
        return dist #regresa el diccionario de distancias

    def kruskal(self):
        e=deepcopy(self.E)
        arbol=Grafo()
        peso=0
        comp=dict()
        t=sorted(e.keys(),key=lambda k:e[k],reverse=True)
        nuevo=set()
        while len(t)>0 and len(nuevo)<len(self.V):
            #print(len(t))
            arista=t.pop()
            w=e[arista]
            del e[arista]
            (u,v)=arista
            c=comp.get(v,{v})
            if u not in c:
                #print('u',u,'v',v,'c',c)
                arbol.conecta(u,v,w)
                peso+=w
                nuevo=c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]=nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol

    
    def vecinoMasCercano(self):
        ni = random.choice(list(self.V))
        result=[ni]
        while len(result) < len(self.V):
            ln = set(self.vecinos[ni])
            le = dict()
            res =(ln-set(result))
            for nv in res:
                le[nv]=self.E[(ni,nv)]
            menor = min(le, key=le.get)
            result.append(menor)
            ni=menor
        return result

   
        

g=Grafo()
g.conecta('a','b', 381)
g.conecta('a','c', 2789)
g.conecta('a','d', 2015)
g.conecta('a','e', 2733)
g.conecta('a','f', 2655)
g.conecta('a','g', 1352)
g.conecta('a','h', 1377)
g.conecta('a','i', 373)
g.conecta('a','j', 2071)
g.conecta('b','c', 2905)
g.conecta('b','d', 2131)
g.conecta('b','e', 3113)
g.conecta('b','f', 2818)
g.conecta('b','g', 1733)
g.conecta('b','h', 1758)
g.conecta('b','i', 753)
g.conecta('b','j', 2275)
g.conecta('c','d', 789)
g.conecta('c','e', 1284)
g.conecta('c','f', 192)
g.conecta('c','g', 1823)
g.conecta('c','h', 1743)
g.conecta('c','i', 2408)
g.conecta('c','j', 709)
g.conecta('d','e', 1377)
g.conecta('d','f', 702)
g.conecta('d','g', 1240)
g.conecta('d','h', 1161)
g.conecta('d','i', 1753)
g.conecta('d','j', 181)
g.conecta('e','f', 1098)
g.conecta('e','g', 1383)
g.conecta('e','h', 1352)
g.conecta('e','i', 2360)
g.conecta('e','j', 1197)
g.conecta('f','g', 1640)
g.conecta('f','h', 1560)
g.conecta('f','i', 2293)
g.conecta('f','j', 594)
g.conecta('g','h', 79)
g.conecta('g','i', 981)
g.conecta('g','j', 1172)
g.conecta('h','i', 1066)
g.conecta('h','j', 1094)
g.conecta('i','j', 1703)


print(g.kruskal())
#print(g.shortests('c'))

#print(g)
k=g.kruskal()
print([print(x,k.E[x]) for x in k.E])

for r in range(10):
    ni=random.choice(list(k.V))
    dfs=k.DFS(ni)
    c=0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs)-1):
        c+=g.E[(dfs[f],dfs[f+1])]
        print(dfs[f],dfs[f+1],g.E[(dfs[f],dfs[f+1])])

    c+=g.E[(dfs[-1],dfs[0])]
    print(dfs[-1],dfs[0],g.E[(dfs[-1],dfs[0])])
    print('costo',c)

vmc = g.vecinoMasCercano()
print(vmc)
c=0
for f in range(len(vmc) -1):
    c += g.E[(vmc[f],vmc[f+1])]
    print(vmc[f], vmc[f+1], g.E[(vmc[f],vmc[f+1])] )
    
c += g.E[(vmc[-1],vmc[0])]
print(vmc[-1], vmc[0], g.E[(vmc[-1],vmc[0])])
print('vmc costo',c)


data=list('abcdefghij')
tim=time.clock()
per=permutation(data)
vm, rm= 100000000000,[]
for e in per:
    #print(e)
    c=0
    for f in range(len(e) -1):
        c += g.E[(e[f],e[f+1])]
        #print(e[f], e[f+1], g.E[(e[f],e[f+1])] )
        
    c += g.E[(e[-1],e[0])]
    #print(e[-1], e[0], g.E[(e[-1],e[0])])
    if c < vm:
        vm,rm= c,e
    #print('e costo',c)
print(time.clock()-tim)
print('minimo exacto',vm,rm)
