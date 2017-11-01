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
        self.fila.append(0,e)
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
        self.V = set()
        self.E = dict()
        self.vecinos = dict()
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos:
            self.vecinos[v] = set()
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso
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
        e=deepcoy(self.E)
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
        lv=list(self.V)
        random.shuffle(lv)
        ni=lv.pop()
        le=dict()
        while len(lv)>=0:
            ln=self.v[ni]
            for nv in ln:
                le[nv]=self.E[(ni,nv)]
            menor=min(le.values())
            lv.append(menor)
            del lv[menor]
        return lv
            

g=Grafo()
g.conecta('a','b', 1)
g.conecta('a','c', 1)
g.conecta('a','d', 1)
g.conecta('a','e', 1)
g.conecta('c','e', 1)
g.conecta('c','f', 10)
g.conecta('b','f', 1)

print(g.kruskal())
print(g.shortests('c'))

print(g)
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

data=list('abcdefghij')
tim=time.clock()
per=permutation(data)
print(time.clock()-tim)

                              
            
        
    
                    
                    
