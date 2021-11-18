#une liste est une collection d'objets indexés


liste1 = [5, 7, "toto", True, -2.7]
print(liste1)

#accèder à un élément par indice
print(liste1[2])

#on peut compter à partir de la fin 
print(liste1[-1])
print(liste1[-3])

#concaténation 
print([3,2,1,]+[6,5,4])

#ajout d'un élément en fin liste 
liste1.append("dernier")
print(liste1)

#taille liste
print(len(liste1))

#supp un élément
liste1.remove("toto")
print(liste1)
print()

liste1.reverse()
print(liste1)


liste1 = [5, 7, "toto", True, -2.7]

#parcure liste par valeur 
for element in liste1:
    print(element)
print()

#parcure liste par indice 
for i in range(len(liste1)):
    print(i,liste1)
print()

#création liste élément par élément 
liste2=[]
for i in range(7):
    liste2.append(2**i)
print(liste2)



"""
Exercice 
créer une liste et remplir avec trois str
donnes par l'utilisateur 
"""

list=[]
for i in range(3):
    element=input("donner une chaine")
    list.append(element)
print(list)


"""
créer une liste et la remplir avec 
des nombres donnés par 
l'utilisateur jsq stop  
"""

list=[]
element=input("entrez un nbr : ")
while element != "stop":
    list.append(element)
    element=input("entrez un nbr : ")
print(list)



