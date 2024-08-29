num=int(input())
for i in range(1,num//2):
    if (num==i*(i+1)):
        f=True
        break
    else:
        f=False
print("Pronic Number" if f else "Not Pronic Number")
