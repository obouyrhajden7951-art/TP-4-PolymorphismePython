from abc import ABC, abstractmethod


class Paiement(ABC):
    def __init__(self, somme):
        if somme <= 0:
            raise ValueError("Le montant doit être strictement positif.")
        self._somme = float(somme)

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):
    def __init__(self, somme, num_carte, code_cvv):
        super().__init__(somme)
        if not self._luhn_valide(num_carte):
            raise ValueError("Numéro de carte invalide.")
        if not (code_cvv.isdigit() and len(code_cvv) == 3):
            raise ValueError("CVV invalide.")
        self._num_carte = num_carte
        self._code_cvv = code_cvv

    @staticmethod
    def _luhn_valide(num):
        """Vérification de Luhn simplifiée."""
        if not num.isdigit() or len(num) < 13:
            return False
        somme_chiffres = 0
        for pos, car in enumerate(reversed(num)):
            val = int(car)
            if pos % 2 == 1:
                val *= 2
                if val > 9:
                    val -= 9
            somme_chiffres += val
        return somme_chiffres % 10 == 0

    def payer(self):
        return f"Paiement par carte bancaire de {self._somme:.2f} € (carte **** {self._num_carte[-4:]}) confirmé."


class PayPal(Paiement):
    def __init__(self, somme, adresse_mail, jeton_api):
        super().__init__(somme)
        if "@" not in adresse_mail:
            raise ValueError("E-mail invalide.")
        if not jeton_api:
            raise ValueError("Token d'API invalide.")
        self._adresse_mail = adresse_mail
        self._jeton_api = jeton_api

    def payer(self):
        return f"Paiement PayPal de {self._somme:.2f} € (compte {self._adresse_mail}) confirmé."


class Crypto(Paiement):
    RESEAUX = ("BTC", "ETH", "SOL")

    def __init__(self, somme, id_portefeuille, nom_reseau):
        super().__init__(somme)
        if not id_portefeuille:
            raise ValueError("Identifiant de portefeuille invalide.")
        if nom_reseau not in Crypto.RESEAUX:
            raise ValueError(f"Réseau non supporté : {nom_reseau}")
        self._id_portefeuille = id_portefeuille
        self._nom_reseau = nom_reseau

    def payer(self):
        return f"Paiement Crypto de {self._somme:.2f} € sur le réseau {self._nom_reseau} (wallet {self._id_portefeuille}) confirmé."


def traiter_paiements(liste_paiements):
    for p in liste_paiements:
        print(p.payer())


if __name__ == "__main__":
    liste_paiements = [
        CarteBancaire(120.50, "4539578763621486", "123"),
        CarteBancaire(45.00, "4556737586899855", "456"),
        PayPal(80.00, "alice@example.com", "tok_abc123"),
        PayPal(15.99, "bob@example.com", "tok_xyz789"),
        Crypto(300.00, "0xA1B2C3", "ETH"),
        Crypto(50.00, "bc1qxyz789", "BTC"),
    ]

    traiter_paiements(liste_paiements)