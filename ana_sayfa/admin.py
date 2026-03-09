from django.contrib import admin
from .models import TeknoProje

@admin.register(TeknoProje)
class TeknoProjeAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'eklenme_tarihi', 'durum')
    # Listede doğrudan tıklanabilir checkbox olması için:
    list_editable = ('durum',)