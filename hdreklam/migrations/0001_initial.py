# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Banner'
        db.create_table('hdreklam_banner', (
            ('baslik', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('olusturulma', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('resim', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('yazar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('yayindami', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('bitis', self.gf('django.db.models.fields.DateTimeField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('sef_baslik', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('aciklama_sef', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aciklama', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('hdreklam', ['Banner'])

        # Adding model 'TextLink'
        db.create_table('hdreklam_textlink', (
            ('bitis', self.gf('django.db.models.fields.DateTimeField')()),
            ('sira', self.gf('django.db.models.fields.IntegerField')()),
            ('olusturulma', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('yazar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('yayindami', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('baslik', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('sef_baslik', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('aciklama_sef', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aciklama', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('hdreklam', ['TextLink'])

        # Adding model 'TanitimYazisi'
        db.create_table('hdreklam_tanitimyazisi', (
            ('yazar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('degistirilme', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('olusturulma', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('resim', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('yayindami', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('baslik', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sef_baslik', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('icerik', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('aciklama_sef', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aciklama', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('hdreklam', ['TanitimYazisi'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Banner'
        db.delete_table('hdreklam_banner')

        # Deleting model 'TextLink'
        db.delete_table('hdreklam_textlink')

        # Deleting model 'TanitimYazisi'
        db.delete_table('hdreklam_tanitimyazisi')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 13, 9, 47, 1, 593000, tzinfo=<UTC>)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 13, 9, 47, 1, 593000, tzinfo=<UTC>)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hdreklam.banner': {
            'Meta': {'object_name': 'Banner'},
            'aciklama': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'aciklama_sef': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bitis': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'olusturulma': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'resim': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sef_baslik': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'yayindami': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'yazar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'hdreklam.tanitimyazisi': {
            'Meta': {'object_name': 'TanitimYazisi'},
            'aciklama': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'aciklama_sef': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'degistirilme': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'icerik': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'olusturulma': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'resim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sef_baslik': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'yayindami': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'yazar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'hdreklam.textlink': {
            'Meta': {'object_name': 'TextLink'},
            'aciklama': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'aciklama_sef': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bitis': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'olusturulma': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sef_baslik': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sira': ('django.db.models.fields.IntegerField', [], {}),
            'yayindami': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'yazar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }
    
    complete_apps = ['hdreklam']
