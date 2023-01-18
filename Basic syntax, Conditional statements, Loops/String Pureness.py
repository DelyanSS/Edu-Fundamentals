n = int(input())

for i in range(n):
    string = input()
    if any(c in string for c in ",._"):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")