arr={8,3,6,4,2,5,7,1}
def quicksort(arr):#se define la funcion quicksort con la cantidad de elemntos a trabajar la cual es nombrada arr
	if len(arr)<=1:#si la cantidad de elementos que se encuentra en arr es menor igual a uno se realiza lo siguiente 
		return arr
	piv=arr[0]# se selecciona el pivote a trabajar (lo mas recomendable es seleccionar el que se ubica en la primera poscicion)
	izquierda=[]# los numeros que ocuparan el arreglo izquierda al momento de ser comparadas con pivote
	derecha=[]# los numeros que ocuparan el arreglo derecha al momento de ser comparadas con pivote
	for i in range (1,len(arr)):#se hace un ciclo para seleccionar a los numeros que compararemos con pivote los cuales deben ser los que se encuentran despues de el hasta la ultima poscicion del arreglo
		if (arr[i]<piv):# si el numero ubicado en tal posicion cumple con esto se acomodara en el lado izquiero del arreglo
			izquierda.append(arr[i])
		else:
			derecha.append(arr[i]) # si el numero no cumple la condicion anterior se acomodara por consiguiente en el lado derecho

l={8,3,6,4,2,5,7,1}
def quicksort(l,first,last):
#definimos los indices y calculamos el pivote
i=fisrt
j=last
pivote=(l[i]+l[j])/2
#iteramos hasta que i no sea menor que j
	while (i<j):
#iteramos mientras que el valor de l[i] sea menor que pivote
	while (l[i]<pivote):
	#incrementamos el indice
	i+=1
	#iteramos mientras que el valor de l[j] sea mayor que pivote
	while (l[j]>pivote):
	#decrementamos el indice
	j-=1
	#si i es menor que j significa que los indices se han cruzado
	if (i<=j):
	#creamos una variable temporal para guardar eñ valor de l[j]
	x=l[j]
	#intercambiamos los valores de l[j] y l[i]
	l[j]=l[i]
	l[i]=x
	#incrementamos y decrementamos i y j respectivamente
	i+=1
	j-=1
	#si first es menor que j mantenemos la recursividad 
	if (first<j):
		l=quicksort (l,first,j)
	#si last es mayor que i mantenemos la recursividad
	if (last>i):
		l=quicksort (l,i,last)
	#devolvemos la lista ordenada 
	return l




