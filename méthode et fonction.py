# une méthode est une fonction qui appartien à un objet 
liste=["gh","ie","zr"]
sorted(liste) # fonction, n'agit pas directement sur la liste 
liste.sort() # méthode
# les objet muable c'est à dire qu'on peut modifier (listes, dictionnaires, sets)
# les objet immuable c'est à dire qu'on ne peut modifier (chaines de caractères; nombres) pour les modifier il faut créer de nouveau objet 
print(len("python"))
print(len(['4',4,7]))
print(round(2.2),round(2.7))
print(min([3,7,8]), max([3,7,8]), max("berz"), min("berz"), sum([3,7,8]))
a= range(5,2) 
print(a)