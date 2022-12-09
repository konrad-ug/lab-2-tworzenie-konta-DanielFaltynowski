import unittest

from ..Konto import *

class testZaciaganieKredytu(unittest.TestCase):

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