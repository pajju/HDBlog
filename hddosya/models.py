from django.db import models
from unidecode import unidecode

class Dosyalar(models.Model):
   DOSYA_RESIMLERI = (
	('c','C'),
	('cplus','C++'),
	('eklenti','Eklenti'),
	('exe','Exe'),
	('gif','Gif'),
	('header','Header'),
	('html','Html'),
	('java','Java'),
	('jpeg','Jpeg'),
	('js','Js'),
	('mp3','Mp3'),
	('pdf','Pdf'),
	('php','Php'),
	('plain','Plain'),
	('png','Png'),
	('python','Python'),
	('script','Bash Script'),
	('sifreli','Sifreli'),
	('text','Text'),
	('widget','Widget'),
	('xml','Xml'),
	('zip','Zip/Rar'),	
   )
   
   baslik    	    = models.CharField(max_length=255, verbose_name="Baslik", help_text = "Dosya Basligi")
   sef_baslik	    = models.CharField(max_length=255, verbose_name="Baslik Sef", help_text = "Baslik Sef", blank=True) 
   slug      	    = models.SlugField(max_length=255, verbose_name="Slug")
   
   aciklama    	    = models.TextField(max_length=500, verbose_name="Aciklama", help_text = "Dosya Aciklamasi")
   aciklama_sef	    = models.TextField(max_length=500, verbose_name="Aciklama Sef", help_text = "Aciklama Sef", blank=True)
   
   dosya			= models.FileField(upload_to="upload/")
   dosya_turu 	    = models.CharField(max_length=10, verbose_name="Dosya Turu", help_text = "Dosya Turu", blank=True)
   dosya_resim	    = models.CharField(max_length=255, verbose_name="Dosya Resmi", help_text = "Dosya Resmi", choices=DOSYA_RESIMLERI) 
   
   dosya_kaynak		= models.CharField(max_length=255, verbose_name="Dosya Kaynagi", help_text = "Dosya Kaynagi", blank=True)
   
   gizli			= models.BooleanField(verbose_name="Dosya Gizli Mi?", default=False, help_text = "Dosya Gizli Mi?")
   
   olusturulma 	    = models.DateTimeField(auto_now_add=True, verbose_name="Olusturulma Tarihi")
   degistirilme		= models.DateTimeField(auto_now=True, verbose_name="Degistirilme Tarihi")

   def __unicode__(self):
       return self.baslik
	   
   def save(self, *args, **kwargs):
       self.sef_baslik = unidecode(self.baslik)
       super(Dosyalar, self).save(*args, **kwargs)
	   
       self.aciklama_sef = unidecode(self.aciklama)
       super(Dosyalar, self).save(*args, **kwargs)	   
	   
   class Meta:
	   verbose_name_plural = "Dosyalar"
	   
   def get_absolute_url(self):
	   return "/dosya/%s/" %self.slug