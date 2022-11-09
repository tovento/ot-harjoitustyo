import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_alustetaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.edulliset, 0)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_kateisosto_onnistuu(self):
        osto = self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(osto, 260)

        self.assertEqual(self.kassapaate.edulliset, 1)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaan_lounaan_kateisosto_onnistuu(self):
        osto = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(osto, 100)

        self.assertEqual(self.kassapaate.maukkaat, 1)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullisen_lounaan_kateisosto_epaonnistuu_jos_raha_ei_riita(self):
        osto = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(osto, 200)

        self.assertEqual(self.kassapaate.edulliset, 0)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_kateisosto_epaonnistuu_jos_raha_ei_riita(self):
        osto = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(osto, 300)

        self.assertEqual(self.kassapaate.maukkaat, 0)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_lounaan_korttiosto_onnistuu(self):
        osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(osto, True)

        self.assertEqual(
                str(self.maksukortti),
                "Kortilla on rahaa 7.60 euroa")

        self.assertEqual(self.kassapaate.edulliset, 1)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_korttiosto_onnistuu(self):
        osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertTrue(osto)

        self.assertEqual(
                str(self.maksukortti),
                "Kortilla on rahaa 6.00 euroa")

        self.assertEqual(self.kassapaate.maukkaat, 1)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_lounaan_korttiosto_epaonnistuu_jos_raha_ei_riita(self):
        kortti = Maksukortti(200)

        osto = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertFalse(osto)

        self.assertEqual(
                str(kortti),
                "Kortilla on rahaa 2.00 euroa")

        self.assertEqual(self.kassapaate.edulliset, 0)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_korttiosto_epaonnistuu_jos_raha_ei_riita(self):
        kortti = Maksukortti(300)

        osto = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertFalse(osto)

        self.assertEqual(
                str(kortti),
                "Kortilla on rahaa 3.00 euroa")

        self.assertEqual(self.kassapaate.maukkaat, 0)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataaminen_onnistuu(self):
        lataus = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(
                str(self.maksukortti),
                "Kortilla on rahaa 15.00 euroa")

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortin_lataaminen_epaonnistuu_negatiivisella_summalla(self):
        lataus = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(
                str(self.maksukortti),
                "Kortilla on rahaa 10.00 euroa")

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
