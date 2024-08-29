num=int(input())
n,tot=num,0
while(n>0):
    tot+=n%10
    n//=10
print("Harshad Number" if tot%9==0 else "Not Harshad Number")
    
