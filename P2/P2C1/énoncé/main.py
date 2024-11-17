def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    nombre_a_gauche = 0
    nombre_a_droite = 2
    symbole = "/"
    resultat = 0
    
    if isinstance(nombre_a_droite, int) and isinstance(nombre_a_gauche, int) != True :
        print("les nombres saisis ne sont pas entier!!! GAME OVER")
        exit()
    
    match symbole :
        case "+" :
            resultat = nombre_a_gauche + nombre_a_droite
        case "-" :
            resultat = nombre_a_gauche - nombre_a_droite
        case "*" : 
            resultat = nombre_a_gauche * nombre_a_droite
        case "/":
            if nombre_a_droite == 0:
                print("division par zéro impossible!!!")
                exit()
            else:
                resultat = nombre_a_gauche / nombre_a_droite
        case _:
            print("inconito battaillon!!!")
            exit()
    
    print(f"le résultat de l'opération est : {resultat}")      


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
    
#Créez deux variables  nombre_a_gauche  et  nombre_a_droite  , et affectez-leur chacune un nombre entier.

#Créez une variable  symbole  pour stocker le symbole d'opération (+, -, * ou /).

#Créez une dernière variable  resultat  initialisée à 0, qui contiendra ensuite le résultat du calcul.

#Vérifiez que les deux variables  nombre_a_gauche  et  nombre_a_droite  sont bien des nombres entiers. Si l'une ou les deux ne sont pas des entiers, affichez un message d'erreur correspondant et quittez le programme. (Aide : Utiliser la fonction  isinstance()  )

#Vérifiez que le symbole stocké dans la variable  symbole  correspond bien à une des 4 opérations autorisées (+, -, * ou /) à l’aide du  match. Si le symbole n'est pas correct, affichez un message d'erreur correspondant, et quittez le programme.

#Attention, il est impossible de diviser un nombre par 0, il faut donc prévoir une structure conditionnelle supplémentaire pour vérifier ce cas dans la structure  match. Utilisez les conditions if-else pour réaliser cette opération ; s’il y a une division par 0, affichez  Erreur: impossible de diviser par zéro. , sinon stockez le calcul dans la variable  resultat.

#Affichez le résultat contenu dans la variable  resultat.