from django.contrib import admin
from django import forms
from hdyazi.models import Yazilar, Kategoriler
from hdmakale.models import Makaleler, mKategoriler
from hdsayfalar.models import Sayfalar
from hddosya.models import Dosyalar
from hdlink.models import Link
from hdduyuru.models import Duyurular
from django.db import models

class KategoriAdmin(admin.ModelAdmin):
	list_display = ('baslik','aciklama','kategori_resim')
	prepopulated_fields = {"slug": ("baslik",)}

class YazilarAdmin(admin.ModelAdmin):
   list_display = ('baslik','yazar','kategori','aciklama','olusturulma','degistirilme')
   prepopulated_fields = {"slug": ("baslik",)}
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',)

class mKategoriAdmin(admin.ModelAdmin):
	list_display = ('baslik','aciklama','kategori_resim')
	prepopulated_fields = {"slug": ("baslik",)}
	
class MakalelerAdmin(admin.ModelAdmin):
   list_display = ('baslik','yazar','kategori','aciklama','olusturulma','degistirilme')
   prepopulated_fields = {"slug": ("baslik",)} 
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',)  

class SayfalarAdmin(admin.ModelAdmin):
   list_display = ('baslik','yazar','aciklama','olusturulma','degistirilme')
   prepopulated_fields = {"slug": ("baslik",)}
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',)		

class DosyaAdmin(admin.ModelAdmin):
	list_display = ('baslik','aciklama','dosya_kaynak')
	prepopulated_fields = {"slug": ("baslik",)}
	
class LinkAdmin(admin.ModelAdmin):
	list_display = ('link','hits','get_short_id')
	
class DuyurularAdmin(admin.ModelAdmin):
   list_display = ('baslik','yazar','aciklama','olusturulma','degistirilme')
   prepopulated_fields = {"slug": ("baslik",)} 
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',)  	
	
admin.site.register(Yazilar, YazilarAdmin)
admin.site.register(Kategoriler, KategoriAdmin)
admin.site.register(Makaleler, MakalelerAdmin)
admin.site.register(mKategoriler, mKategoriAdmin)
admin.site.register(Sayfalar, SayfalarAdmin)
admin.site.register(Dosyalar, DosyaAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Duyurular,DuyurularAdmin)