class Konto:
    def __init__(self):
        self.saldo = None


    def calc_saldo(self, kod, pesel):
        if kod != None and kod[0:5] == "PROM_":
            if pesel[2] == "2" or pesel[2] == "3":
                return 50
            else:
                if int(pesel[0:2]) > 60:
                    return 50
        return 0


    def wyplac(self, kwota):
        if kwota <= self.saldo:
            self.saldo = self.saldo - kwota



    def wplac(self, kwota):
        self.saldo = self.saldo + kwota

class KontoPrywatne(Konto):
    def __init__(self, imie, nazwisko, pesel, kod=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.kod = kod
        self.saldo = self.calc_saldo(self.kod, self.pesel)


    def wyplac_express(self, kwota):
        if kwota <= self.saldo:
            self.saldo = self.saldo - kwota - 1


class KontoFirmowe(Konto):
    def __init__(self, nazwa, nip):
        super().__init__()
        self.nazwa = nazwa
        self.nip = nip
        self.saldo = 0

    def wyplac_express(self, kwota):
        if kwota <= self.saldo:
            self.saldo = self.saldo - kwota - 5



