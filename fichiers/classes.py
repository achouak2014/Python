

class Personne:
    ###constructeur 
    ## tout les méthode declasse prend un parametre
    def __init__(self,nom):
        ###initialiser les attribut
        self.nom=nom
        self.argent=0
    ## nouvel methode
    def present_toi(self):
        print("bonjour, je m'appelle ",self.nom)

    def get_argent(self):
        return self.argent

p1 = Personne("chouchou")
print(p1.nom)

p2 = Personne("chouchou")
print(p2.nom)
p2.present_toi() #equivalent à Personne.presente_toi(p2)


print(p2.get_argent())

