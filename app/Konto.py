import datetime


def calc_saldo(kod, pesel):
    if kod != None and kod[0:5] == "PROM_":
        if pesel[2] == "2" or pesel[2] == "3":
            return 50
        else:
            if int(pesel[0:2]) > 60:
                return 50
    return 0
class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.kod = kod
        self.saldo = calc_saldo(self.kod, self.pesel)





