def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    saisie = input("saisissez une liste de nombres séparés par des virgules (par exemple : 1,2,3,4)")
    liste_nombre = [int(nombre) for nombre in saisie.split(",")]
    print(f" liste des nombres : {liste_nombre}")
         
    somme = 0
    for nombre in liste_nombre:
        somme += nombre
        
    print(f"La somme de tous les nombres est : {somme}")
    
    moyenne = somme/len(liste_nombre)
    print(f"La moyenne est : {moyenne}")
    
    for nombre in liste_nombre:
        if nombre > moyenne:
            print(f"{nombre} est au dessus de la moyenne !")   
        
    for nombre in liste_nombre:    
        if (nombre % 2) == 0:
            print(f"{nombre} est un nombre pair")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
    
#Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : 1,2,3,4), et affichez cette liste.

#Calculez et affichez la somme des nombres dans la liste.

#Calculez et affichez la moyenne des nombres dans la liste.

#Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.

#Calculez et affichez le nombre de nombres dans la liste qui sont pairs