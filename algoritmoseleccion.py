arr={6,4,2,1,3,5}
import random
cnt=0
def selection(arr):
global cnt
	for i in range( 0,len(arr)-1):#se recorre hasta len(arr)-1 porque el ultimo elemento no es necesario ordenarlo
		min=i #el primer elemento por defaut es el minimo por lo pronto
		for j in range(i+1,len(arr)):#aqui se recorre con los demas elementos para preguntarles si tu eres el minimo
				cnt+=1
			if arr[j]<arr[min]:#aqui se hace la comprobacion si en verdad encontramos el minimo comparandolo con el primer elemnto minimo defaut
				min=j #en caso de que se cumpla la desigualdad este sera el nuevo minimo
			temp=arr[i]# primero se guarda uno de los valores a una variable temporal
			arr[i]=arr[min]# luegos  nos llevamos uno de los valores a las posiciones que hemos guardado antes 
			arr[min]=temp# finalmente se hace el cambio en el otro sentido 
	return arr
	return cnt
		
	
	print(arr,selection,cnt)
	