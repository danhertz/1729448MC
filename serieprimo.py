def seriePrimo(numPrimo):
    c=0
    i=0
    while c<numPrimo:
        i+=1
        if esPrimo(i):
            c+=1
            print(i)

print seriePrimo(10)
