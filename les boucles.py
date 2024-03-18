for i in [4,3,3,7,4]:
    print(i)
for i in range(7) :
    print("bonjour")
i=0
while i<7:
    print("salut".capitalize())
    i+=1
liste = ["1","4","3","paul","25","pierre"]
for element in liste :
    if element.isdigit():
        continue # n'arrête pas l'execution de la boucle elle fait que passer à la prochaine itération
    print(element)
for element in liste :
    if element.isdigit():
        break # permet de sortir de la boucle 
    print(element)
liste = [2,1, 3, 4, 5, -4, -3, -6]
nombr_positif = [i for i in liste if i>0] # compréssion de liste 
print(nombr_positif)

# EXERCICES 1
nombre = [1,21,5,44,4,9,5,83,29,31,25,38]
nombres_paires = [i for i in nombre if i%2 == 0]
print(nombres_paires)

# EXERCICE 2
nombres = range(-10,10)
nombre_positifs = [i for i in nombres if i >= 0]
print(nombr_positif)

# EXERCICE 3
nombres = range(5)
nombre_doubles = [i*2 for i in nombres]
print(nombre_doubles)

#EXERCICE 4
nombres = range(10)
nombre_inverses = [-i if i >= 0 else i for i in nombres  ]
print(nombre_inverses)

 # EXERCICE 4
i = 1 
while i<=10 :
    print("utlisateur "+ str(i))
    i+=1

nombre = range(1,11)
numero_utilisateur = [print("utlisateur " + str(i)) for i in nombre]
mot = "python"
mot = reversed(mot)
for i in mot :
    print(i) 

continu = "O"
while continu == "O" :
    print("on continu !")
    continu = input("Voulez vous continuer ? O/N:  ")
    continu = continu.upper()


