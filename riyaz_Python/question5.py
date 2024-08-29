num=int(input())
n=num
_1=0
while(n>0):
    _1+=((n%10)**2)
    n//=10
i=1
while(i*i<_1):
    i+=1
print("Beautiful" if (i*i)==_1 else "Not Beautiful")
