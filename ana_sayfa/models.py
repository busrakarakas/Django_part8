from django.db import models

class TeknoProje(models.Model):
    baslik = models.CharField(max_length=200)
    detay = models.TextField()
    # Integer yerine Boolean kullanıyoruz
    durum = models.BooleanField(default=False, verbose_name="Tamamlandı mı?")
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)
    resim = models.ImageField(upload_to='projeler/', blank=True, null=True)

    def __str__(self):
        return self.baslik