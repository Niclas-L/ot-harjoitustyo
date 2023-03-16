import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_setup(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset, self.kassapaate.maukkaat), (100000, 0, 0))

    def test_edullinen_kateisella_riittavasti(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihto, self.kassapaate.edulliset), (100240, 60, 1))
    
    def test_edullinen_kateisella_ei_riittavasti(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihto, self.kassapaate.edulliset), (100000, 200, 0))
    
    def test_maukkaan_kateisella_riittavasti(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihto, self.kassapaate.maukkaat), (100400, 100, 1))
    
    def test_maukkaan_kateisella_ei_riittavasti(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihto, self.kassapaate.maukkaat), (100000, 200, 0))

    def test_edullinen_kortilla_riittavasti(self):
        x = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.edulliset, self.maksukortti.saldo, self.kassapaate.kassassa_rahaa, x), (1, 760, 100000, True))
    
    def test_edullinen_kortilla_ei_riittavasti(self):
        kortti = Maksukortti(200)
        x = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual((self.kassapaate.edulliset, kortti.saldo, self.kassapaate.kassassa_rahaa, x), (0, 200, 100000, False))

    def test_maukkaan_kortilla_riittavasti(self):
        x = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.maukkaat, self.maksukortti.saldo, self.kassapaate.kassassa_rahaa, x), (1, 600, 100000, True))
    
    def test_maukkaan_kortilla_ei_riittavasti(self):
        kortti = Maksukortti(200)
        x = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual((self.kassapaate.maukkaat, kortti.saldo, self.kassapaate.kassassa_rahaa, x), (0, 200, 100000, False))

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.maksukortti.saldo), (100100, 1100))

    def test_lataa_rahaa_kortille_hylatty(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.maksukortti.saldo), (100000, 1000))