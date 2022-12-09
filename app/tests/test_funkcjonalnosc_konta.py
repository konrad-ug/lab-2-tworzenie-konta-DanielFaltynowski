import unittest

from ..Konto import *


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


    def test_konto_firmowe_wyplata_mozliwa1(self):
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


    def test_konto_firmowe_wyplata_mozliwa2(self):
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