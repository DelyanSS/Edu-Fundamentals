while True:
    command = input()
    if command == "Welcome!":
        break
    if command == "Voldemort":
        print("You must not speak of that name!" )
        exit()
    if command == "Welcome":
        print("Welcome to Hogwarts.")
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")
print("Welcome to Hogwarts.")

