n = int(input())
max = 0
while n > 0:
    num = n % 10
    if num > max:
        max = num
    n //= 10
    break
print(max)

    
