# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:31:03 2017

@author:Luis Daniel Honorato Hernandez 
"""


import random
import copy

def burbuja (arr):
    cnt=0
    for recorrido in range(0,len(arr)-1):
    	for posicion in range(0,len(arr)-1):
    		cnt+=1
    		if (arr[posicion]>arr[posicion+1]):
    			temp=arr[posicion]
    			arr[posicion]=arr[posicion+1]
    			arr[posicion+1]=temp 
    return cnt

def ins(arr):
    cnt=0
    for indice in range(1,len(arr)):
    		valor=arr[indice] 
    		i=indice-1  
    		while (i>=0): 
    			cnt=cnt+1
    			if (valor<arr[i]): 
    				arr[i+1]=arr[i] 
    				arr[i]=valor 
    				i=i-1 
    			else:
    				break
    return cnt

def selection(arr):
   cnt=0
   for i in range( 0,len(arr)-1):
       minimo=i 
       for j in range(i+1,len(arr)):
           cnt+=1
           if arr[j]<arr[minimo]:
               minimo=j 
       temp=arr[i]
       arr[i]=arr[minimo]
       arr[minimo]=temp 
   return cnt

##funcion que nos genera numeros aleatorios
def num_ale(cuantos):
    arreglo=[]
    for  i in range(cuantos):
        arreglo.append(random.randint(0,100))
    return arreglo

def quicksort(arr):
    global cnt
    cnt+=1
    if len(arr)<=1:
        return arr
    piv=arr[0]
    izquierda=[]
    derecha=[]
    for i in range (1,len(arr)):
        #cnt+=1
        if(arr[i]<piv):
            izquierda.append(arr[i])
        else:
            derecha.append(arr[i]) 
    return quicksort(izquierda)+[piv]+quicksort(derecha)
global cnt    
l=2
print("Longitud","Burbuja","Selection","Insertion","Quicksort")
while l < 1002:
    arreglo = num_ale(l)
    l1,l2,l3,l4= copy.deepcopy(arreglo), copy.deepcopy(arreglo), copy.deepcopy(arreglo), copy.deepcopy(arreglo)
    b= burbuja(l1)
    i=ins(l2)
    s=selection(l3)
    cnt = 0
    quicksort(l4)
    print(l,b,s,i,cnt)
    l = l + 25
    



