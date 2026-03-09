from django.test import TestCase
from django.urls import reverse
from .models import TeknoProje

class ProjeTestleri(TestCase):
    
    # Her testten önce çalışacak hazırlık verisi
    def setUp(self):
        self.proje = TeknoProje.objects.create(
            baslik="Test Projesi",
            detay="Bu bir test detayıdır.",
            durum=True
        )

    # Ana sayfanın çalışıp çalışmadığını test et
    def test_anasayfa_gorunumu(self):
        response = self.client.get(reverse('anasayfa'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Projesi")

    # Detay sayfasının çalışıp çalışmadığını test et
    def test_proje_detay_gorunumu(self):
        response = self.client.get(reverse('proje_detay', args=[self.proje.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bu bir test detayıdır.")