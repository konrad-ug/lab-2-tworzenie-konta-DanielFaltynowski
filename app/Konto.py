class Konto:
    def __init__(self):
        self.saldo = None
        self.historia = []


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
            self.historia.append(-kwota)



    def wplac(self, kwota):
        self.saldo = self.saldo + kwota
        self.historia.append(kwota)



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
            self.historia.append(-kwota)
            self.historia.append(-1)


    def zaciagnij_kredyt(self, kwota):
        if len(self.historia) < 5:
            return False
        test1 = self.historia[-3] > 0 and self.historia[-2] > 0 and self.historia[-1] > 0
        test2 = self.historia[-5] + self.historia[-4] + self.historia[-3] + self.historia[-2] + self.historia[-1] > kwota
        if test1 and test2:
            self.saldo += kwota
            return True
        else:
            return False


class KontoFirmowe(Konto):
    def __init__(self, nazwa, nip):
        super().__init__()
        self.nazwa = nazwa
        self.nip = nip
        self.saldo = 0

    def wyplac_express(self, kwota):
        if kwota <= self.saldo:
            self.saldo = self.saldo - kwota - 5
            self.historia.append(-kwota)
            self.historia.append(-5)


    def zaciagnij_kredyt(self, kwota):
        test1 = sum(self.historia) >= 2 * kwota
        test2 = -1775 in self.historia
        if test1 and test2:
            self.saldo += kwota
            return True
        else:
            return False





