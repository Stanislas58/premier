liste = [ True, 45, "essono"]
liste.append("ok")
liste.extend([4,8])
liste.remove(45)
print(liste)
a = liste[0]
b= liste[-5]
print(a,b)
e,f = liste[2],liste[-3]
print(e,f)
print( liste[:])# debut et fin
print(liste[:-1])
print(liste[0:1])# cette fonction exclusive ne tien pas comte du dernier élément
print(liste[::2])# permet de prendre un élément sur 2, 2 aui représente le pas
print(liste[::-1])# permet d'inverser une liste
print(liste.index("ok"))# fonction qui renvois le rand de l'élément dans ma liste 
liste.append("essono") 
print(liste.count("essono"))# fonction qui compte le nombre d'occurence de l'"l"ment dans ma liste 
liste.remove(4)
liste.remove(8)
liste.remove(True)
liste.sort() # permet de trier par ordre alphabetique, elle ne retourne rien donc ne peut être  affecté 
print(liste)
liste.extend(["vane", 'manger'])
print(liste)
liste_trier = sorted (liste)
print(liste_trier)
liste.reverse()
print(liste)# inverse le contenu de la liste
le_seul=liste.pop(-1) # retire le dernier élément et affecte à le_seul
print(liste)
print(le_seul)
liste.clear()
print(liste)
liste2 = ["bonjour","je","veux","manger"]
liste = " - ".join(liste2)
print(liste)
print(dir(list))
caractère = "moi,ou,toi,"
liste3=list(caractère)
print(liste3)
print("moi" in liste2)
print("moi" in caractère)
liste = ["java",["python","c++",["pascal"]],"ruby"]
print(liste[1][2])
print(liste[1][2][0])
print(liste[0][0:2])# une chaine de caractère est une liste de caractères 