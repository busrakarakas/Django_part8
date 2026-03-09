from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # Bunu import etmeyi unutma!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ana_sayfa.urls')),
]

# Medya dosyaları için gerekli yol:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)