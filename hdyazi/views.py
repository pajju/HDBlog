from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from hdyazi.models import *
from hdmakale.models import *
from hdsayfalar.models import *
from hddosya.models import *
from hdduyuru.models import *
from django.contrib.sites.models import Site
from django.db.models import Q
from tagging.models import Tag, TaggedItem

def home(request):
	yazilar = Yazilar.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()	
	return render_to_response('index.html', locals())

def kategori(request, slug):
	kategori = get_object_or_404(Kategoriler, slug=slug)
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	yazilar = Yazilar.objects.filter(kategori=kategori.id).filter(anasayfa_sabit=True).order_by("-olusturulma")	
	kategoriler = Kategoriler.objects.order_by("baslik")
	mkategoriler = mKategoriler.objects.order_by("baslik")
	makaleler = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")	
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()	
	return render_to_response('kategori.html', locals())		
	
def yazi(request):
	yazilar = Yazilar.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")
	kategoriler = Kategoriler.objects.order_by("baslik")
	makaleler = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")	
	mkategoriler = mKategoriler.objects.order_by("baslik")
	sayfalar = Sayfalar.objects.order_by("baslik")
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()
	return render_to_response('single.html', locals())

def post(request, slug):
	yazi = get_object_or_404(Yazilar, slug=slug)
	kategoriler = Kategoriler.objects.order_by("baslik")
	mkategoriler = mKategoriler.objects.order_by("baslik")
	makaleler = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()
	return render_to_response('post.html', locals())

def etiket(request, tag_name):
	tag = get_object_or_404(Tag, name=tag_name)
	yazilar = TaggedItem.objects.get_by_model(Yazilar, tag).filter(anasayfa_sabit=True)
	kategoriler = Kategoriler.objects.order_by("baslik")
	mkategoriler = mKategoriler.objects.order_by("baslik")
	makaleler = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")	
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()
	return render_to_response('etiket.html', locals())

def makale(request, slug, kat_slug):
	makale = get_object_or_404(Makaleler, slug=slug)
	mkategoriler = mKategoriler.objects.order_by("baslik")
	bkategoriler = Kategoriler.objects.order_by("baslik")
	listmakale = Makaleler.objects.order_by("-olusturulma")
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()
	return render_to_response('makale.html', locals())
	
def mkategori(request, kat_slug):
	kategori = get_object_or_404(mKategoriler, slug=kat_slug)	
	makaleler = Makaleler.objects.filter(kategori=kategori.id).filter(anasayfa_sabit=True).order_by("-olusturulma")	
	maklist	= Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")	
	kategoriler = mKategoriler.objects.order_by("baslik")
	bkategoriler = Kategoriler.objects.order_by("baslik")
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")	
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()	
	return render_to_response('mkategori.html', locals())	
	
def metiket(request, tag_name):
	tag = get_object_or_404(Tag, name=tag_name)
	makaleler = TaggedItem.objects.get_by_model(Makaleler, tag).filter(anasayfa_sabit=True)
	maklist = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	mkategoriler = mKategoriler.objects.order_by("baslik")
	kategoriler = Kategoriler.objects.order_by("baslik")
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()
	return render_to_response('metiket.html', locals())	

def sayfalar(request, slug):
	sayfa = get_object_or_404(Sayfalar, slug=slug)
	kategoriler = Kategoriler.objects.order_by("baslik")
	mkategoriler = mKategoriler.objects.order_by("baslik")
	makaleler = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")	
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()	
	return render_to_response('sayfa.html', locals())
		
def makaleler(request):
	makaleler = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")
	kategoriler = Kategoriler.objects.order_by("baslik")
	mkategoriler = mKategoriler.objects.order_by("baslik")
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	listmakale = Makaleler.objects.order_by("-olusturma")
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()
	return render_to_response('msingle.html', locals())	

def dosya(request, slug):
	dosya = get_object_or_404(Dosyalar, slug=slug)
	mkategoriler = mKategoriler.objects.order_by("baslik")
	bkategoriler = Kategoriler.objects.order_by("baslik")
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	listmakale = Makaleler.objects.order_by("-olusturulma")
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()	
	return render_to_response('dosya.html', locals())		
	
def dosyalar(request):
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	makaleler = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")
	kategoriler = Kategoriler.objects.order_by("baslik")
	mkategoriler = mKategoriler.objects.order_by("baslik")
	listmakale = Makaleler.objects.order_by("-olusturma")
	sayfalar = Sayfalar.objects.order_by("baslik")
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	site = Site.objects.get_current()	
	return render_to_response('dosyalar.html', locals())	

def duyuru(request, slug):
	duyuru = get_object_or_404(Duyurular, slug=slug)
	kategoriler = Kategoriler.objects.order_by("baslik")
	mkategoriler = mKategoriler.objects.order_by("baslik")
	makaleler = Makaleler.objects.filter(anasayfa_sabit=True).order_by("-olusturulma")
	dosyalar = Dosyalar.objects.filter(gizli=False).order_by("-olusturulma")
	sayfalar = Sayfalar.objects.order_by("baslik")
	site = Site.objects.get_current()
	duyurular = Duyurular.objects.order_by("-olusturulma")
	
	return render_to_response('duyuru.html', locals())	