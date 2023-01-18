#Write a program that reads different floating-point numbers from the console. When it receives a number between 1 and
# 100 inclusive, the program should stop reading and should print "The number {number} is between 1 and 100".

while True:
    num = float(input())
    if num >= 1 and num <= 100:
        print(f"The number {num} is between 1 and 100")
        break