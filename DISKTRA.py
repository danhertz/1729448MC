from heapq import heapoop,heappush

def flatten(L):
    while len(L)>0:
        yield L[0]
        L=L[1]

class Grafo:
    def__init__(self):
        self.V=set()#un conjunto
        self.E=dict()#un mapeo de pesos de aristas
        self.vecinos=dict()#un mapeo

    def agrega(self,v):
        self.V.add(v)
        if not v in self.vecinos:#inicialmente no tiene nada

    def conecta(self,v,u,peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v,u)]=self.E[(u,v)]=peso #en ambos sentidos}
        self.vecinos[v].add(u)
        self.vecinos[u].add[v]

    def complemento(self):
        comp=Grafo()
        for v in self.V:
            for w in self.V:
                if v!=w and(v,w) not in self.E:
                    comp.conecta(v,w,1)
        return comp

    def shortest(self,v):#algoritmo de dijkstra
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
                    el=self.E[(u,n)]#se toma la distancia del nodo actual mas la distancia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
                    
