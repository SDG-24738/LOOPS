print("1. Bike")
print("2. Car")
print("Select one of these options")
selection = int(input("Enter your choice"))
if selection == 1:
    print("What type")
    print("1. sports bikes")
    print("2. motocross")
    choose = int(input("Choose your option"))
    if choose == 1:
        print("You like sport's bikes")
    else:
        print("You like motocross")
elif selection == 2:
    print("What type")
    print("1. Bugati")
    print("2. Rolls Royce phantom")
    choose = int(input("Choose ypur option"))
    if choose == 1:
        print("You like bugati")
    else:
        print("You like rolls royce phantom")
else:
    print("Invalid option")
