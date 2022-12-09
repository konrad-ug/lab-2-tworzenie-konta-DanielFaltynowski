import unittest

from parameterized import parameterized

from ..Konto import *

class test_kredyt_parameterized(unittest.TestCase):
    imie = "Daniel"
    nazwisko = "Faltynowski"
    pesel = "0226174567"
    nazwa = "Miotek Kompani"
    nip = '1567834529'

    @parameterized.expand([
        ([], 3000, False),
        ([100, 300, 1880, 1750, 1120], 100, True),
        ([1000, -200, 400, 1000, 3000, -250, 120], 100, False),
        ([100, 300, 5000, 2000, -100], 100, False),
        ([3000, -100, 300, 1000, 3000], 200, True),
        ([1000, 2000, 3000], 1000, False),
        ([4000, -1000, 3000, 2000, 1000], 100000, False),
        ([4000, -1000, 3000, 2000, 1000], 1000, True)
    ])
    def test_zaciaganie_kredytu_parameterized(self, historia, kwota, przyznanie):
        konto = KontoPrywatne(self.imie, self.nazwisko, self.pesel)
        konto.historia = historia
        zaciagnij = konto.zaciagnij_kredyt(kwota)
        self.assertEqual(zaciagnij, przyznanie, "Nie spełniono warunków do zaciągnięcia kredytu")


    @parameterized.expand([
        ([], 100, False),
        ([1775, 300, -1775, 100, 600], 500, True),
        ([700, -300, 2000, -1775], 10000, False),
        ([950, -200, 10000], 1000, False),
        ([750, -30, 10000, -1775], 1000000, False),
    ])
    def test_zaciaganie_kredytu_parameterized_firmowe(self, historia, kwota, przyznanie):
        konto = KontoFirmowe(self.nazwa, self.nip)
        konto.historia = historia
        zaciagnij = konto.zaciagnij_kredyt(kwota)
        self.assertEqual(zaciagnij, przyznanie, "Nie spełniono warunków do zaciągnięcia kredytu")