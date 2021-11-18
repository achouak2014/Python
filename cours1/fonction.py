"""
une fonction a 
-un nom
-des paramétres
-éventuellement une valeur de retour 



from types import AsyncGeneratorType


def mafonction(par1,par2):
    var=par1+par2
    return var

reslt = mafonction(2,3)
print(reslt)

print(mafonction("ab",'cd'))


def affiche_zero():
    print(0)

affiche_zero()
z=affiche_zero()
print(z)

"""

"""
exercice 
fonction prend en paramétre une annee de naissance
renvoie la chaine "majeur "ou mineur


def age(annee):
    if(2021-annee>=18):
       return "majeur"
    else:
        return "mineur"

print(age(2000))
"""


"""
exercice2

fonct qui prend en par 2 nbr 
renvoie leur somme si nbr1<nbr2
            produit   nbr1>nbr2



def somme(nbr1,nbr2):
    if nbr1<nbr2 :
        return nbr1+nbr2
    else:
        return nbr1*nbr2


S=somme(10,2)
print(somme(10,2))

"""



""""
exercice

fonct prent en parametre une annee de naissance et age 
renvoi true ou false


def boolean(annee , age ):
    return 2021-annee == age
          

print(boolean(1997,24))

""" 

"""
exercice4
fonct prend en paramètre une str
renvoie le nbr de "e"


def nbr_e(chaine):
    compteur=0
    for i in chaine:
        if i =="e":
            compteur+=1
    return compteur        

print(nbr_e("aezee"))
"""

"""
fonct prend en paramètre deux str 
test si le première contient plus 
de voyelles que 2 
renvoi un boolean 

def voyelle(chai1,chai2):
    comp=0
    comp2=0
    for i in chai1:
        if i in "aeiouyAEIOUY":
            comp+=1

    for i in chai2:
        if i in "aeiouyAEIOUY":
            comp2+=1
    return comp > comp2
print(voyelle("efgiiia","azer"))

"""