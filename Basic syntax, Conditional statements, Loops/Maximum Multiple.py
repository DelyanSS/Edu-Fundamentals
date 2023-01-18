divisor = int(input())
boundary = int(input())
n = boundary

while n > 0:
    if n % divisor == 0:
        print(n)
        break
    n -= 1