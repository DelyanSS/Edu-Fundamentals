cofee_counter = 0
while True:
    line = input()
    if line == "END":
        break

    if line == "coding" or line == "dog" or line == "cat" or line == "movie":
        cofee_counter += 1
    elif line == "CODING" or line == "DOG" or line == "CAT" or line == "MOVIE":
        cofee_counter += 2

if cofee_counter > 5:
    print("You need extra sleep")
else:
    print(cofee_counter)
