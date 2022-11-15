import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
	def setUp(self):
		self.kortti = Maksukortti(1000)

	def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
		kortti = Maksukortti(350)
		kortti.syo_maukkaasti()
		self.assertEqual(str(kortti),"Kortilla on rahaa 3.50 euroa")

	def test_negatiivisen_summan_lataaminen_ei_muuta_saldoa(self):
		self.kortti.lataa_rahaa(-400)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

	def test_kortilla_voi_ostaa_edullisen_lounaan_tasarahalla(self):
		kortti = Maksukortti(250)
		kortti.syo_edullisesti()
		self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

	def test_kortilla_voi_ostaa_maukkaan_lounaan_tasarahalla(self):
		kortti = Maksukortti(400)
		kortti.syo_maukkaasti()
		self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
