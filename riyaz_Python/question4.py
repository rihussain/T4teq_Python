num=int(input())
for i in range(2,(num//2)+1):
    if num%i==0:
        print("Not prime palindrome")
        break
    else:
        print("Prime palindrome" if str(num)==(str(num)[::-1]) else "Not prime palindrome")
        break
