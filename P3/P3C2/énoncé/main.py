# Écrivez votre code ici !
import os
from bs4 import BeautifulSoup

# Construire le chemin du fichier relatif au script Python
repertoire_script = os.path.dirname(os.path.realpath(__file__))
chemin_fichier = os.path.join(repertoire_script, "index.html")

# Extraction des information avec BeautifullSoup
with open(chemin_fichier, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
        
    
title = soup.title.string
h1_texte = soup.find_all('h1')
products = soup.find_all('li')
products_list = []

# Extraction des noms des prix et des descriptions des produits dans la liste    
for product in products:
    name = product.h2.string
    price = product.find('p', string=lambda s: 'Prix' in s).string
    descritpion = product.find('p', string=lambda s: 'Description' in s).string
    products_list.append((name, price, descritpion))


# Affichage des informations extraites    
print("Titre de la page :", title)
print("Texte de la balise h1 :", h1_texte)
print("Liste des produits :", products_list)


# Conversion du prix en Dollars    
for i, (name, price, description) in enumerate(products_list):
    # Supprimer les caractères non numériques de la chaîne de prix
    euro_price_str = ''.join(filter(str.isdigit, price.split()[2])) 
    euro_price = int(euro_price_str)
    dollar_price = euro_price * 1.2
    products_list[i] = (name, f"{dollar_price}$ {descritpion}")

# Affichage des informations mises à jour
print("informations mis à jour :")   
print("Titre de la page :", title)
print("Texte de la balise h1 :", h1_texte)
print("Liste des produits :", products_list)