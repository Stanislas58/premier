a=  6
liste= []
MENU = """ choisisser parmi les 05 obtions suivants
1: Ajouter un élément à la liste
2: Retirer un élément à la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
😃 Votre choix :  """
while  a != 0 : 
    a= input(MENU) 
    a = int(a)
    if a == 1 :
        b= input("Entrer l'élément à ajouter : ")
        liste.append(b)
        print(f"{b} à bien été ajouté à la liste")
    elif a == 2 :
        d= input("Entre le nom de l'élément que vous voulez retirer : ")
        if not d in liste :
            print(f"{d} ne fait pas partir de la liste")
            continue 
        elif d in liste :  
            liste.remove(d)
            print(f"{d} à bien été retiré de la liste")
    elif a == 4 :
        if not liste == []:
            liste.clear() 
            print("La liste à été vidé de son contrenu")
        else :
            print("Votre liste ne contient aucun élément")
    elif a == 3 :
        n = 1
        if not liste == [] :
            print("La lites des éléments: ")
            for i in liste :
              print(f"{n}: {i}")
              n+=1
        else :
          print("Votre liste ne contient aucun élément")  
    elif a == 5 :
        print("A bientôt !")
        break
