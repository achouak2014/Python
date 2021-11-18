"""

#pour écrire dans un fichier with il ferme le bloc a la fin
with open("monfichier.txt","w") as fichier:
    fichier.write("Bonjour toto\n")
    fichier.write("ca va?\n")

#pour écrire à la fin d'un fichier sans écraser le rest
# avec a append
with open("monfichier.txt","a") as fichier:
    fichier.write("troisieme ligne\n")

#pour lire un fichier
with open("monfichier.txt","r") as fichier:
    a=fichier.read()
print(a)
# lire modifier executy

#lire un fichier ligne par ligne
with open("monfichier.txt","r") as fichier:
    lignes=fichier.readlines()
print(lignes)

#pour ne pas avoir de \n
with open("monfichier.txt","r") as fichier:
    l=fichier.read().splitlines()
print(l)


"""
"""
EXECRCICE
Créer un dictionnaire de 5 éléments
dont les clés sont des noms 
et les valeurs sont des notes.
Les notes sont prises au hasard entre 0 et 20
"""
import random
dictionnaire={}
for i in range(5):
    cle=input("Nom : ")
    dictionnaire[cle]=random.randint(0,20)
print(dictionnaire)


"""
EXERCICE 
Sauvgarder ces données dans un fichier notes.txt
avec un nom sur la première ligne, puis une note sue
la deuxiéme, puis un nom sur la troisiéme,ect..

"""
with open("note.txt","w") as fichier:

    for nom in dictionnaire:
        fichier.write(nom+"\n")
        fichier.write(str(dictionnaire[nom])+"\n")

""""
EXERCICE
Lire le fichier et reconstruire un autre dictionnaire
à partir  des données
le nouveau dictionnaire doit être identique au premier
"""

with open("note.txt","r") as fichier:
    lignes=fichier.read().splitlines()
print(lignes)
dictionnaire2={}
for i in range(0,len(lignes),2):
    dictionnaire2[lignes[i]]= int(lignes[i+1])
print(dictionnaire2)
print(dictionnaire==dictionnaire2)













