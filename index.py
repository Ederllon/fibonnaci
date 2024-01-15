icount = int(input('Dígite um número para fazer a sequência de Fibonacci: '))

count = icount - 2   

n1 = int(0) 
n2 = int(1)

print(0 ,end=" ")
print(1 ,end=" ")
while count != 0 :
    n3 = n1 + n2
    print(n3 , end=" ")
    n1 = n2
    n2 = n3
    count = count -1
    

       



