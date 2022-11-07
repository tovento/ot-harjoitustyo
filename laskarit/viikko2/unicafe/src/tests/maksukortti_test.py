import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(
                str(self.maksukortti),
                "Kortilla on rahaa 10.00 euroa")

    def test_kortin_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(
                str(self.maksukortti),
                "Kortilla on rahaa 15.00 euroa")

    def test_rahan_ottaminen_onnistuu_jos_kortilla_riittavasti_rahaa(self):
        test = self.maksukortti.ota_rahaa(500)

        self.assertTrue(test)

        self.assertEqual(
                str(self.maksukortti),
                "Kortilla on rahaa 5.00 euroa")

    def test_saldo_pysyy_samana_jos_raha_ei_riita_ostoon(self):
        test = self.maksukortti.ota_rahaa(2000)

        self.assertFalse(test)

        self.assertEqual(
                str(self.maksukortti),
                "Kortilla on rahaa 10.00 euroa")
