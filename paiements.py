from abc import ABC, abstractmethod


class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être strictement positif.")
        self._montant = float(montant)

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        if not self._luhn_valide(numero):
            raise ValueError("Numéro de carte invalide.")
        if not (cvv.isdigit() and len(cvv) == 3):
            raise ValueError("CVV invalide.")
        self._numero = numero
        self._cvv = cvv

    @staticmethod
    def _luhn_valide(numero):
        """Vérification de Luhn simplifiée."""
        if not numero.isdigit() or len(numero) < 13:
            return False
        total = 0
        for i, chiffre in enumerate(reversed(numero)):
            n = int(chiffre)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    def payer(self):
        return f"Paiement par carte bancaire de {self._montant:.2f} € (carte **** {self._numero[-4:]}) confirmé."


class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        if "@" not in email:
            raise ValueError("E-mail invalide.")
        if not token:
            raise ValueError("Token d'API invalide.")
        self._email = email
        self._token = token

    def payer(self):
        return f"Paiement PayPal de {self._montant:.2f} € (compte {self._email}) confirmé."


class Crypto(Paiement):
    RESEAUX = ("BTC", "ETH", "SOL")

    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        if not wallet_id:
            raise ValueError("Identifiant de portefeuille invalide.")
        if reseau not in Crypto.RESEAUX:
            raise ValueError(f"Réseau non supporté : {reseau}")
        self._wallet_id = wallet_id
        self._reseau = reseau

    def payer(self):
        return f"Paiement Crypto de {self._montant:.2f} € sur le réseau {self._reseau} (wallet {self._wallet_id}) confirmé."


def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())


if __name__ == "__main__":
    paiements = [
        CarteBancaire(120.50, "4539578763621486", "123"),
        CarteBancaire(45.00, "4556737586899855", "456"),
        PayPal(80.00, "alice@example.com", "tok_abc123"),
        PayPal(15.99, "bob@example.com", "tok_xyz789"),
        Crypto(300.00, "0xA1B2C3", "ETH"),
        Crypto(50.00, "bc1qxyz789", "BTC"),
    ]

    traiter_paiements(paiements)