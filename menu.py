def menu():
   try:
        var1 = int(input("Introduce tu primer número:"))
        var2 = int(input("Introduce tu segundo número:"))
        letra = input("Introduce + o -:")

        if letra == "+":
            print(var1+var2)
        elif letra == "-":
            print(var1 - var2)
        else:
            print("Error")
   except ValueError:
       print("No es válido tus números")

menu()
