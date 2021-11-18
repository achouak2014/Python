#renvoie le carré d'un nombre
def carre(x):
    return x**2

#compte le nombre de voyelles dans un texte 
def compt_voyelles(texte):
    cpt=0
    for char in texte:
        if char in "aeiouyAEIOUY":
            cpt+=1
    return cpt

print(__name__)

if __name__ == "__main__":
    print(carre(5))
    print(compt_voyelles("toto"))


