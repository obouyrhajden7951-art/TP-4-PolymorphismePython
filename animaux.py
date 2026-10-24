class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être redéfinie")


class Chien(Animal):
    def parler(self):
        return "Ouaf !"


class Chat(Animal):
    def parler(self):
        return "Miaou !"


def faire_parler(bete):
    print(bete.parler())


liste_animaux = [Chien(), Chat(), Chien()]
for ani in liste_animaux:
    faire_parler(ani)