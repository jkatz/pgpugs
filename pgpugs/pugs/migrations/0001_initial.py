# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('pugs_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(related_name='countries', to=orm['pugs.Region'])),
        ))
        db.send_create_signal('pugs', ['Country'])

        # Adding model 'Pug'
        db.create_table('pugs_pug', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pugs', to=orm['pugs.Country'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('pugs', ['Pug'])

        # Adding model 'Region'
        db.create_table('pugs_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('pugs', ['Region'])


    def backwards(self, orm):
        
        # Deleting model 'Country'
        db.delete_table('pugs_country')

        # Deleting model 'Pug'
        db.delete_table('pugs_pug')

        # Deleting model 'Region'
        db.delete_table('pugs_region')


    models = {
        'pugs.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'countries'", 'to': "orm['pugs.Region']"})
        },
        'pugs.pug': {
            'Meta': {'object_name': 'Pug'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pugs'", 'to': "orm['pugs.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'pugs.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['pugs']
