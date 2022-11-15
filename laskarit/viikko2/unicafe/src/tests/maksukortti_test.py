import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldon_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(50)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.50 euroa")
    
    #rahan ottaminen kortilta toimii oikein

    def test_kortin_saldo_vähenee_jos_kortilla_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_ota_rahaa_palauttaa_true_jos_kortilla_tarpeeksi_rahaa(self):
        kortti=Maksukortti(300)
        self.assertTrue(kortti.ota_rahaa(100))

    def test_metodi_ota_rahaa_palauttaa_false_jos_kortilla_liian_vahan_rahaa(self):
        kortti=Maksukortti(300)
        self.assertFalse(kortti.ota_rahaa(350))