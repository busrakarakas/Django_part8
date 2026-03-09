from django.urls import path
from . import views

urlpatterns = [
    path('', views.ana_sayfa, name='anasayfa'),
    path('proje/<int:id>/', views.proje_detay, name='proje_detay'),
    path('yeni/', views.proje_ekle, name='proje_ekle'),
]