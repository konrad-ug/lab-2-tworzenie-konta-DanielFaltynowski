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




