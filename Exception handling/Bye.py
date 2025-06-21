weather = False
while True:
    try:
         num = int(input("Enter a number"))
         while num%2 == 0:
              print("Bye")
              weather = True
    except ValueError as ex:
         print(ex)
         
