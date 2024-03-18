from pprint import pprint 
import random 
import os # module utilisé pour créer et suprimer des dossiers 
r = random.randint(0, 4) # la fonction retourne une valeur aléatoire entre 0 et 4 
print(r)
r = random.uniform(0, 4) # à la différence de randintn, cette fonction retourne un nombre décimal
print(r)
r = random.randrange(65) # valeur entière entre 0  et 64
t= random.randrange(0, 101, 10) # de 0 à 100 avec un pas de 10
chemin = ""
y = os.path.join(chemin, "dossier 1","le_bon" ) # concaténation de ce qui est dans lea variable chemin avec un nouveau nom de dossier 
z = os.path.join(chemin, "dossier 2")
print(y) 
os.makedirs (y, exist_ok= True)
if not os.path.exists(z) :
    os.mkdir(z)
if os.path.exists(z) :
    os.removedirs(z)
print(dir(os)) # afficher toutes les fonctions qu'on trouve dans le module 
pprint(dir(random)) # affiche les données unpeu plus lisible 
print(callable(os)) # retourne false sii on ne peut pas l'appelé et true dans le cas contraire 
# losque c'est callable ça veux dire c'est une fonction et ça peut prendre des parentèses() et c'est appelable dans le cas contraire c'est un module ou un attribut qui ne peut prendre des ()
# Dans le cas présent il retourne false car on ne peut appeler un module, on appelle des fonction
print(callable(os.path.join))
