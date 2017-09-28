anchura = {1: set([2,3]),
          2: set([4,6]),
          3: set([4,5,7]),
          4: set([5]),
          5: set([6,7]),
          6: set([7,8]),
          7: set([8]),
          8: set([])}#se crea un diccionario que contiene los conjuntos 1,2,3,4,5,6,7,8
def bfs(anchura, '1'): #se llama bfs(busqueda por anchura) que recibe dos par�metros, el gr�fo de anchura que declaramos primero y el nodo desde el que iniciaremos.
   visitado= set([])
   cola=['1'] #ahora dejamos dos variables, el primero ser� un set vacio para nodos visitados y el segundo recibe el nodo desde el que va a iniciar.
   while cola: #es decir, mientras que haya elementos en esta colecci�n
       vertice = cola.pop(0) #creamos una variable que contenga el primer elemento sacado del set 
       if vertice not in visitado: #si este elemento no se encuentra en el set creado para los visitados
           visitado.add(vertice) #entonces se a�ade a ese set
           cola.extend(grafo[vertice] - visitado) #luego se le agregan todos los siguientes elementos de la lista
   return visitado 


profundidad= {1: set([2,3]),
          2: set([4,6]),
          3: set([4,5,7]),
          4: set([5]),
          5: set([6,7]),
          6: set([7,8]),
          7: set([8]),
          8: set([])}#se crea un diccionario que contiene los conjuntos 1,2,3,4,5,6,7,8

def dfs(profundidad, '1'): #se llama dfs(busqueda por profundidad) la funci�n recibe el grafo de profundidad y el nodo inicial
   visitado= set([])
   pila=['1']#Un set para los nodos visitados, y una pila que almacena el nodo que va en turno
   while pila: #mientras haya elementos en la pila�
       vertice = pila.pop() #El v�rtice que guarda el �ltimo elemento de la colecci�n en la pila, a diferencia del otro ya no es el elemento 0, si no el que est� al final
       if vertice not in visitado: #si este elemento no se encuentra en el set creado para los visitados
           visitado.add(vertice) #a�adimos al listado de nodos visitados
           pila.extend(grafo[vertice] - visitado) #a�adimos el siguiente set de la lista.
   return visitado
