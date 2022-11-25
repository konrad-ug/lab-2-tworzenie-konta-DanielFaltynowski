import unittest

from ..Konto import *

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta1(self):
        pierwsze_konto = KontoPrywatne("Dariusz", "Januszewski", "93031278264")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta2(self):
        pierwsze_konto = KontoPrywatne("Dariusz", "Januszewski", "93031278264", "PRM_XYZ")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta3(self):
        pierwsze_konto = KontoPrywatne("Dariusz", "Januszewski", "93031278264", "PROM_XYZ")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 50, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta4(self):
        pierwsze_konto = KontoPrywatne("Dawid", "Jankowski", "02260344582")
        self.assertEqual(pierwsze_konto.imie, "Dawid", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Jankowski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta5(self):
        pierwsze_konto = KontoPrywatne("Dawid", "Jankowski", "02260344582", "PROMDP")
        self.assertEqual(pierwsze_konto.imie, "Dawid", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Jankowski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta6(self):
        pierwsze_konto = KontoPrywatne("Dawid", "Jankowski", "02260344582", "PROM_DP")
        self.assertEqual(pierwsze_konto.imie, "Dawid", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Jankowski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 50, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta7(self):
        pierwsze_konto = KontoPrywatne("Jan", "Kowalski", "01322567529")
        self.assertEqual(pierwsze_konto.imie, "Jan", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Kowalski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta8(self):
        pierwsze_konto = KontoPrywatne("Jan", "Kowalski", "01322567529", "DAJTAPIENIENDZE")
        self.assertEqual(pierwsze_konto.imie, "Jan", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Kowalski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta9(self):
        pierwsze_konto = KontoPrywatne("Jan", "Kowalski", "01322567529", "PROM_DAJTAPIENIENDZE")
        self.assertEqual(pierwsze_konto.imie, "Jan", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Kowalski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 50, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta10(self):
        pierwsze_konto = KontoPrywatne("Paweł", "Wiesłowski", "47052166529")
        self.assertEqual(pierwsze_konto.imie, "Paweł", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Wiesłowski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta11(self):
        pierwsze_konto = KontoPrywatne("Paweł", "Wiesłowski", "47052166529", "EXP")
        self.assertEqual(pierwsze_konto.imie, "Paweł", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Wiesłowski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


    def test_tworzenie_konta12(self):
        pierwsze_konto = KontoPrywatne("Paweł", "Wiesłowski", "47052166529", "PROM_EXP")
        self.assertEqual(pierwsze_konto.imie, "Paweł", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Wiesłowski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")


class TestFunkcjonalnoscKonta(unittest.TestCase):

    def test_przelew_wychodzący_brak_środków(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11], "Niepoprawne dane konta!")
        konto.saldo = 0

        # deposits and withdraws
        konto.wyplac(100)
        self.assertEqual(konto.saldo, 0, "Złe działanie funkcji")


    def test_przelew_wychodzący_obliczanie_srodkow_niewykonalny(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11], "Niepoprawne dane konta!")
        konto.saldo = 50

        # deposits and withdraws
        konto.wyplac(100)
        self.assertEqual(konto.saldo, 50, "Złe działanie funkcji")


    def test_przelew_wychodzący_obliczanie_srodkow_wykonalny(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11], "Niepoprawne dane konta!")
        konto.saldo = 1000

        # deposits and withdraws
        konto.wyplac(100)
        self.assertEqual(konto.saldo, 900, "Złe działanie funkcji")


    def test_wplata(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11],
                         "Niepoprawne dane konta!")

        # deposits and withdraws
        konto.wplac(100)
        self.assertEqual(konto.saldo, 100, "Złe działanie funkcji!")


    def test_seria_przelewow(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11],
                         "Niepoprawne dane konta!")

        # deposits and withdraws
        konto.wplac(100)
        konto.wyplac(250)
        self.assertEqual(konto.saldo, 100, "Złe działanioe funkcji!")
        konto.wyplac(50)
        self.assertEqual(konto.saldo, 50, "Złe działanioe funkcji!")
        konto.wplac(300)
        konto.wyplac(700)
        self.assertEqual(konto.saldo, 350, "Złe działanioe funkcji!")
        konto.wyplac(300)
        self.assertEqual(konto.saldo, 50, "Złe działanioe funkcji!")


    def test_konto_firmowe_wyplata_niemozliwa(self):
        # initial
        konto = KontoFirmowe("Miotek Company", "0123456789")
        self.assertEqual(len(konto.nip), 10, "Niepoprawny NIP!")
        konto.saldo = 50

        # deposit and withdraw
        konto.wyplac(100)
        self.assertEqual(konto.saldo, 50, "Złe działanie funkcji")


    def test_konto_firmowe_wyplata_mozliwa(self):
        # initial
        konto = KontoFirmowe("Miotek Company", "0123456789")
        self.assertEqual(len(konto.nip), 10, "Niepoprawny NIP!")
        konto.saldo = 100

        # deposit and withdraw
        konto.wyplac(10)
        self.assertEqual(konto.saldo, 90, "Złe działanie funkcji")

    def test_konto_firmowe_wyplata_bez_srodkow(self):
        # initial
        konto = KontoFirmowe("Miotek Company", "0123456789")
        self.assertEqual(len(konto.nip), 10, "Niepoprawny NIP!")

        # deposit and withdraw
        konto.wyplac(10)
        self.assertEqual(konto.saldo, 0, "Złe działanie funkcji")


    def test_konto_firmowe_wyplata_mozliwa(self):
        # initial
        konto = KontoFirmowe("Miotek Company", "0123456789")
        self.assertEqual(len(konto.nip), 10, "Niepoprawny NIP!")

        # deposit and withdraw
        konto.wplac(100)
        konto.wyplac(250)
        self.assertEqual(konto.saldo, 100, "Złe działanioe funkcji!")
        konto.wyplac(50)
        self.assertEqual(konto.saldo, 50, "Złe działanioe funkcji!")
        konto.wplac(300)
        konto.wyplac(700)
        self.assertEqual(konto.saldo, 350, "Złe działanioe funkcji!")
        konto.wyplac(300)
        self.assertEqual(konto.saldo, 50, "Złe działanioe funkcji!")


    def test_konto_prywatne_ekspres_brak(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11],
                         "Niepoprawne dane konta!")

        # func
        konto.wyplac_express(10)
        self.assertEqual(konto.saldo, 0, "Złe działanioe funkcji!")

    def test_konto_prywatne_ekspres_niepowodzenie(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11],
                         "Niepoprawne dane konta!")
        konto.saldo = 30

        # func
        konto.wyplac_express(100)
        self.assertEqual(konto.saldo, 30, "Złe działanioe funkcji!")

    def test_konto_prywatne_ekspres_powodzenie(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11],
                         "Niepoprawne dane konta!")
        konto.saldo = 100

        # func
        konto.wyplac_express(10)
        self.assertEqual(konto.saldo, 89, "Złe działanioe funkcji!")


    def test_konto_firmowe_ekspres_brak(self):
        # initial
        konto = KontoFirmowe("Miotek Company", "0123456789")
        self.assertEqual(len(konto.nip), 10, "Niepoprawny NIP!")

        # func
        konto.wyplac_express(10)
        self.assertEqual(konto.saldo, 0, "Złe działanioe funkcji!")


    def test_konto_firmowe_ekspres_niepowodzenie(self):
        # initial
        konto = KontoFirmowe("Miotek Company", "0123456789")
        self.assertEqual(len(konto.nip), 10, "Niepoprawny NIP!")
        konto.saldo = 15

        # func
        konto.wyplac_express(100)
        self.assertEqual(konto.saldo, 15, "Złe działanioe funkcji!")


    def test_konto_firmowe_ekspres_powodzenie(self):
        # initial
        konto = KontoFirmowe("Miotek Company", "0123456789")
        self.assertEqual(len(konto.nip), 10, "Niepoprawny NIP!")
        konto.saldo = 100

        # func
        konto.wyplac_express(10)
        self.assertEqual(konto.saldo, 85, "Złe działanioe funkcji!")


class TestHistorii(unittest.TestCase):
    def test_konto_firmowe_historia(self):
        # initial
        konto = KontoFirmowe("Miotek Company", "0123456789")
        self.assertEqual(len(konto.nip), 10, "Niepoprawny NIP!")
        konto.saldo = 10000
        konto.wyplac(100)
        konto.wyplac_express(50)
        konto.wplac(30)

        # func
        self.assertEqual(konto.historia, [-100, -50, -5, 30], "Niepoprawnie zaksięgoiwana historia")


    def test_konto_prywatne_historia(self):
        # initial
        konto = KontoPrywatne("Daniel", "Faltynowski", "02261734567")
        self.assertEqual([konto.imie, konto.nazwisko, len(konto.pesel)], ["Daniel", "Faltynowski", 11],
                         "Niepoprawne dane konta!")
        konto.saldo = 10000
        konto.wyplac(100)
        konto.wyplac_express(50)
        konto.wplac(30)

        # func
        self.assertEqual(konto.historia, [-100, -50, -1, 30], "Niepoprawnie zaksięgoiwana historia")


class test_zaciaganie_kredytu(unittest.TestCase):

    imie = "Daniel"
    nazwisko = "Faltynowski"
    pesel = "0226174567"

    def test_kredyt_prywatne_konto_brak(self):
        konto = KontoPrywatne(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.zaciagnij_kredyt(1000), False, "Nie spełniono warunków do zaciągnięcia kredytu")


    def test_kredyt_prywatne_konto_nie_spelnione(self):
        konto = KontoPrywatne(self.imie, self.nazwisko, self.pesel)
        konto.wplac(100000)
        konto.wyplac(100)
        konto.wyplac(3000)
        konto.wplac(1000)
        konto.wyplac(100)
        konto.wplac(10)
        self.assertEqual(konto.zaciagnij_kredyt(1000), False, "Nie spełniono warunków do zaciągnięcia kredytu")


    def test_kredyt_prywatne_konto_spelnione(self):
        konto = KontoPrywatne(self.imie, self.nazwisko, self.pesel)
        konto.wplac(100000)
        konto.wyplac(100)
        konto.wyplac(3000)
        konto.wplac(1000)
        konto.wyplac(100)
        konto.wplac(10)
        konto.wplac(10000)
        konto.wplac(1000)
        self.assertEqual(konto.zaciagnij_kredyt(1000), True, "Nie spełniono warunków do zaciągnięcia kredytu")


    def test_kredyt_prywatne_konto_niespelniony_jeden_warunek(self):
        konto = KontoPrywatne(self.imie, self.nazwisko, self.pesel)
        konto.wplac(100000)
        konto.wyplac(100)
        konto.wyplac(3000)
        konto.wplac(1000)
        konto.wyplac(100)
        konto.wplac(10)
        konto.wplac(10)
        konto.wplac(10)
        self.assertEqual(konto.zaciagnij_kredyt(1000), False, "Nie spełniono warunków do zaciągnięcia kredytu")
