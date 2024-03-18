mdp = input("entrer un mot de passe (min 8 caractères):")
mdp_trop_court = "votre mot de passe est trop court."
if len(mdp) == 0 : 
    print(mdp_trop_court.upper())
elif len(mdp) < 8 : 
    print(mdp_trop_court.capitalize())
elif mdp.isdigit():
    print("votre mot de passe ne comptien que des nombre".capitalize())
else :
    print("inscription est terminé".capitalize())
    
    