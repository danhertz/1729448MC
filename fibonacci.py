def fibonacci (n):
    global cnt
    cnt+=1
    if n==0 or n==1:
        return (1)
    return fibonacci (n-2)+fibonacci(n-1)

for i in range (1,51):
    cnt=0
    fibonacci(i)
    print (i,cnt)
    
