Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def minimo(arr):
... x=arr[0]
... for z in arr:
... 	if(z<x):
...		x=z
... return z
...
>>>> def ordenar(arr):
... 	arrsort=[]
...	for z in range(len(arr)):
...		z=minimo(arr)
...		arr.remove(z)
... 		arrsort.append(z)
... return arrsort
SyntaxError: expected an indented block
>>> cnt=0
def minimo(arr):
    k=arr[0]
    global cnt
    for w in arr:
        cnt+=1
        if(w<k):
            k=w
    return k

def ordenar(arr):
    aux=arr[:]
    arrsort=[]
    for k in range(len(aux)):
        w=minimo(aux)
        aux.remove(w)
        arrsort.append(w)
    return arrsort

import random
p=random.sample(range(0,100),40)
print(p)
psort=ordenar(p)
print(cnt)
print(psort)
SyntaxError: multiple statements found while compiling a single statement
>>> cnt=0
def minimo(arr):
    z=arr[0]
    global cnt
    for x in arr:
        cnt+=1
        if(x<z):
            z=x
    return z

def ordenar(arr):
    aux=arr[:]
    arrsort=[]
    for z in range(len(aux)):
        x=minimo(aux)
        aux.remove(z)
        arrsort.append(z)
    return arrsort

import random
p=random.sample(range(0,100),40)
print(p)
psort=ordenar(p)
print(cnt)
print(psort)
SyntaxError: multiple statements found while compiling a single statement
>>> 
