print("ok "*3)
print(10%3)# modulo permet d'obtenir le reste d'une division
print(10/3)
print(10//3)# division entière 
print(2**4)# puissance
i=0
i=+1 # incrémentation à 1 équivalent à i=i+1
# il existe aussi i=-1, i/=10, i=*1, i**=5, i//=1
print(i)
g=40
g//=3
print(g)
i+=3
print(i)
print(g!=i)
print(g==i)
print(g<=i)
print(g>=i)
a,b=[1,2,3],[1,2,3]
print(a==b) # permet de comparer l'égalité des valeurs qui sont contenu dans nos variables 
print(a is b) # permet de vérifier si deux objet sont les mêmes en mémoire: les adresses sont différentes 
print(id(a),id(b) )
d,e=-30000.455,-30000.455 
g,f=[3,6],[3,6]
print(d is e)
print(f is g)
print(id(d),id(e))
z,w="esso",6
print(f" Bonjour {z}, combien font {w}+{e}") # méthode f-string
print(f" C'est égale à {w+e}")
print(" Bonjour {1}, comment tu {0} ?".format("vas","Vanéssa")) # méthode format
bonjour = "Bonjour {prénom} vous avez regardé {nom_videos} vidéos cette semaine."
aurevoir = "A bientôt {prénom}"
user = input("Entrez le nom d'utilisateur:")
vidéo = 5
print(bonjour.format(prénom=user, nom_videos=vidéo )) 
premier_nbre=int(input("Entrez le premier nombre : "))
deuxième_nbre=int(input("Entrez le deuxième nombre : "))
somme = premier_nbre + deuxième_nbre
division = premier_nbre / deuxième_nbre
soustraction = premier_nbre - deuxième_nbre
multiplication = premier_nbre * deuxième_nbre
print("la somme de {0} avec {1} est égale à {2}".format(premier_nbre,deuxième_nbre,somme))
print("la soustration de {0} par {1} est égale à {2}".format(premier_nbre,deuxième_nbre,soustraction))
print("la division de {0} par {1} est égale à {2}".format(premier_nbre,deuxième_nbre,division))
print("la multiplication de {0} par {1} est égale à {2}".format(premier_nbre,deuxième_nbre,multiplication))
print(f"la somme de {premier_nbre} avec {deuxième_nbre} est egale à {premier_nbre + deuxième_nbre}")