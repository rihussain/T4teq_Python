num=int(input())
power=len(str(num))
n,tot=num,0
while(n>0):
    tot+=((n%10)**power)
    power-=1
    n//=10
print("Disarium number" if (tot==num) else "Not Disarium Number")
