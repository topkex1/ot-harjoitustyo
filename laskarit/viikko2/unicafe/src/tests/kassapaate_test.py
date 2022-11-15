import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(100)

    def test_kassa_olemassa(self):
        self.assertIsNotNone(self.kassa)

    def test_luodun_kassan_rahamaara_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa,100000)

    def test_luodun_kassan_myydyt_edulliset_lounaat_oikein(self):
        self.assertEqual(self.kassa.edulliset,0)

    def test_luodun_kassan_myydyt_maukkaat_lounaat_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    #käteisostojen testit

    def test_syo_edullisesti_kateisella_palauttaa_maksun_jos_kateinen_ei_riita(self):
        maksu=200
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(maksu), maksu)
    
    def test_syo_edullisesti_kateisella_ei_muuta_myytyjen_edullisten_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_syo_edullisesti_kateisella_ei_muuta_myytyjen_maukkaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_palauttaa_maksun_jos_kateinen_ei_riita(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300), 300)

    def test_syo_maukkaasti_kateisella_ei_muuta_myytyjen_edullisten_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullisesti_palauttaa_vaihtorahat_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(260), 260-240)

    def test_syo_edullisesti_kateisella_muuttaa_myytyjen_edullisten_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(260)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_syo_maukkaasti_kateisella_palauttaa_vaihtorahat_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(450), 50)
    
    def test_syo_maukkaasti_kateisella_muuttaa_myytyjen_maukkaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.maukkaat, 1)

    #korttiostot

    def test_syo_edullisesti_kortilla_palauttaa_false_jos_saldo_ei_riita(self):
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(self.kortti))

    def test_syo_maukkaasti_kortilla_palauttaa_false_jos_saldo_ei_riita(self):
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(self.kortti))

    def test_syo_maukkaasti_kortilla_ei_veloita_kortilta_jos_saldo_ei_riita(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")

    def test_syo_edullisesti_kortilla_ei_veloita_kortilta_jos_saldo_ei_riita(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")

    def test_syo_edullisesti_kortilla_ei_muuta_edullisten_maaraa_jos_saldo_ei_riita(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_syo_maukkaasti_kortilla_ei_muuta_maukkaiden_maaraa_jos_saldo_ei_riita(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullisesti_kortilla_veloittaa_oikein_jos_saldo_riittaa(self):
        self.kortti.lataa_rahaa(400)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.60 euroa")

    def test_syo_maukkaasti_kortilla_veloittaa_oikein_jos_saldo_riittaa(self):
        self.kortti.lataa_rahaa(400)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")

    def test_syo_edullisesti_palautta_true_jos_saldo_riittaa(self):
        self.kortti.lataa_rahaa(400)
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.kortti))

    def test_syo_maukkaasti_palautta_true_jos_saldo_riittaa(self):
        self.kortti.lataa_rahaa(400)
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.kortti))

    def test_syo_edullisesti_kortilla_muuttaa_edullisten_maaraa_oikein_kun_saldo_riittaa(self):
        self.kortti.lataa_rahaa(400)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_maukkaasti_kortilla_muuttaa_maukkaiden_maaraa_oikein_kun_saldo_riittaa(self):
        self.kortti.lataa_rahaa(400)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_edullisesti_kassa_ei_muutu_jos_saldo_ei_riita(self):
        kassa = self.kassa.kassassa_rahaa
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa,kassa)

    def test_syo_maukkaasti_kassa_ei_muutu_jos_saldo_ei_riita(self):
        kassa = self.kassa.kassassa_rahaa
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa,kassa)

    def test_syo_edullisesti_kortilla_kassa_ei_muutu_jos_saldo_riittaa(self):
        kassa = self.kassa.kassassa_rahaa
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, kassa)

    def test_syo_maukkaasti_kortilla_kassa_ei_muutu_jos_saldo_riittaa(self):
        kassa = self.kassa.kassassa_rahaa
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, kassa)
        
    #kortin lataaminen

    def test_lataa_rahaa_kortille_muuttaa_kortin_saldoa_oikein_kun_summa_positiivinen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 300)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 4.00 euroa")
    
    def test_lataa_rahaa_kortille_kassa_kasvaa_summalla_kun_summa_positiivinen(self):
        kassa=self.kassa.kassassa_rahaa
        self.kassa.lataa_rahaa_kortille(self.kortti,300)
        self.assertEqual(self.kassa.kassassa_rahaa,kassa + 300)

    def test_lataa_rahaa_kortille_palauttaa_none_jos_summa_negatiivinen(self):
        self.assertIsNone(self.kassa.lataa_rahaa_kortille(self.kortti, -50))

    def test_lataa_rahaa_kortille_ei_muuta_saldoa_jos_summa_negatiivinen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -50)
        self.assertEqual(str(self.kortti),"Kortilla on rahaa 1.00 euroa")

    def test_lataa_rahaa_kortille_ei_muuta_kassaa_jos_summa_negatiivinen(self):
        kassa = self.kassa.kassassa_rahaa
        self.kassa.lataa_rahaa_kortille(self.kortti, -50)
        self.assertEqual(self.kassa.kassassa_rahaa, kassa)