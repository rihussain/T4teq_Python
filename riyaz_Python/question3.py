a,b,c=int(input()),int(input()),int(input())
if a==b==c:
    print("Equilateral")
elif a==b or a==c or b==c:
    print("Isosceles")
else:
    print("Scalene")
