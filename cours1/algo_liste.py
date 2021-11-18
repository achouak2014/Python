
list=[3,6,9,5,7,8,4]
print(list)
print("max",max(list))
print("min",min(list))
print("somme",sum(list))
print("nb de 3", list.count(3))

"""
Exercice:
Sans utiliser les fonction ci-dessus,réécrire
les fonction avec des boucles
"""

#renvoie le plus petit élément de la liste 
liste=[3,6,9,5,-7,7,8,4]

def minimum(liste):
    min=liste[0]
    for i in (liste):
        if(i<min):
            min=i
    return min

print(minimum(liste))


#renvoie la somme des éléments de la liste 
liste=[1,2,3,4,50,100]
def sommes(liste):
    somme=0
    for i in liste:
        somme+=i;
    return somme
print(sommes(liste))



#renvoie le nombre d'occurences de la valeur dans la liste
liste=[1,2,3,4,50,4,100]
def compte(liste,valeur):
    resultat=0
    for element in liste:
        if element == valeur:
            resultat+=1
    return resultat 

print(compte(liste,4))
#renvoie True si tous les élément sont >=0
#false si au moins un élément est négatif
def tous_positifs(liste):
    for element in liste:
        if element<0:
            return False
    return True
print(tous_positifs(liste))

"""
ecrire une fonction qui prend en paramètre
deux entiers n et d et qui teste
 si d est un diviseurde n 
"""

def test_dev(n,d):
    return n%d==0 
print("ok",test_dev(10,5))

"""
ecrire une fonction qui prend en paramètre un entier n 
et qui renvoie la liste de ses diviseurs 
"""

def diviseur(n):
    #on parcourt tous les nombres de 1 à n inclus
    for i in range(1,n+1):
        #si on trouve n diviseur de n 
        if diviseur(n,1):
            #on l'ajoute à la liste 
            liste.append(i)
    return liste
print(diviseur(12))

""""
Ecrire une fonction qui prend en paramètre un entier n 
et qui test si n est premiier 
rapel : un nombre premier possede exactement 2 diviseur
"""

def premier(n):
    return len(diviseur(n))==2
print(premier(12))
print(premier(1))


"""
EXERCICE
afficer la liste des nombres premiers inférieurs à 100
"""

premier=[]
for i in range(100):
    if premier(i):
        premier.append(i)
print(premier)