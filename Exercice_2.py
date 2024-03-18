n= 0
while n==0 :
    nombre1 = input("entrer le premier nombre : ")
    nombre2 = input("entrer le deuxième nombre: ")
    if nombre1.isdigit() and nombre2.isdigit():
        print(f"addition de {nombre1} et de {nombre2} est égale à {int(nombre1) + int(nombre2)}")
        break
    elif not nombre1.isdigit()  or not nombre2.isdigit() :
        print("Entrez les deux nombres valides : ")