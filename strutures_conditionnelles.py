âge = int(input("Entré votre âge : "))
if âge >= 18 : 
    print("vous êtes majeurs !")
elif âge <= 13 :
    print("vous êtes adoléscent")
else:
    print("vous êtes mineur")
print("vrai") if âge >= 18 else print("false")
