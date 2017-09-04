def ordenamiento_ por_insercion_(array):#array es la cantidad del numero de elementos
	for indice in range(1,len(array)):#se empieza con el elemento 1 ya que no tiene caso iniciarlo en 0  porque no se puede comparar con un elemento antes de este
		valor=array[indice]#es el valor ocupado en en el indice 2 a comparar con el valor de la izquierda 
		i=indice-1 # es el indice que se encuentra antes que el anterior para realizar la comparacion 
		while (i>=0): # se debe cumplir esta condicion para realizar lo que esta dentro del programa
			if (valor<array[i]): # se compara que el segundo valor sea menor al primer valor si no es asi se sale de la condicion
				array[i+1]=array[i] # el valor que se encuentra en la segunda poscion sera intercambiado por el valor de la primera posicion
				array[i]=valor #el valor  de la primera posicion ocupara el lugar del valor de la segunda posicion
				i=i-1 #se disminuye un indice y se vuelve a revisar la condicion anterior si no se cumple se sale del ciclo 
			else:
				break
#PROGRAMA INSERCION
array={2,1,3,5}
print(array)
print(ordenamiento_por_insercion)