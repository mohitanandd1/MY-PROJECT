num=int(input("enter a number: "))
n=num
total=0
nod=len(str(n))
while n>0:
    ld=n%10
    total=total+(ld**nod)
    n=n//10
print(total==num)