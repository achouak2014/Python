

print("hello ,world")
v1=3
v2=5
print(3+5)
print ("la premier variable est ", v1, "le la deuxieme variable est " , v2 )

#conversion de type 
mastring="abc"+str(v1)
print(mastring)


"""
Exercice
Demander à l'utilisateur d'entrer son année de naissance
et afficher quel anniversaire il va fêter en 2021
"""

annee = int(input("Entrez la date de naissance : ") )
age = 2021 - annee
print ("Tu à ", age ,"ans ")

entree=float(input("Entrer un nombre "))
if entree>=0:
    print("positif")
else:
    print("négatif")
if entree>=0:
    print("positif")
elif entree<0: 
    print("négatif")

"""
Exercice
demander à l'utilisateur son âge
afficher "mineur" ou "majeur" suivant s'il a moins ou plus
de 18 ans ou afficher "menteur" si le nombre est négatif
ou s'il est plus grand que 130
"""
age = int(input("Quel âge as-tu ? "))

if(age<0 or age >130):
    print("Menteur")
elif age >=18:
    print("Major")
    
else:
    print("mineur")



print ("h" in "haroun")
print ("wiss" not in "achouak")

print (not False)
print (True and  False)
print (True or False)
print (True and  True)

print(3<2 or "to" in "toto ")

