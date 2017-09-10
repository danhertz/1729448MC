import random
cnt=0
def burbuja (lista):#(lista) es la cantidad de elementos que contiene la lista 
global cnt
for recorrido in range(1,len(lista)-1):#es el recorrido del arreglo menos una cantidad de elementos 
	for posicion in range(0,len(lista)-1):#es la posicion del arreglo menos una cantidad de elementos
		cnt=cnt+1
		if (lista[posicion]> lista[posicion+1]):#se hace la comparacion del valor que esta en la posicion  de la lista con el otro para ver si es mayor y si lo es se cambian ya que asi es el metodo burbuja por ejem (18>9) 
			temp=lista[posicion]#la variable temporal sirve para guardar el valor mayor de la posicion comparada en el paso anterior por ejem(18 ahora es variable temporal)
			lista[posicion]=lista[posicion+1]#el primer elemento  comparado se reemplaza por el segundo 
			lista[posicion+1]=temp # el segundo elemento es la variable temporal
	print (lista)
lista={4,12,8,2,1}

#PROGRAMA BUBBLE

print (lista)
burbuja(lista)
lista={4,12,8,2,1}


def burbuja(A):
	for i in range (0,valor):
		i=valor
	if(A[i]>(A[i+1]
		else
	[i]=i
#PROGRAMA BUBBLE 2
print (lista)
burbuja(lista)
A={4,12,8,2,1}
