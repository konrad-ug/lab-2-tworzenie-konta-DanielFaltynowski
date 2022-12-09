import unittest

from ..Konto import *

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