# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Post'
        db.create_table('pugs_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['pugs.Author'])),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('pugs', ['Post'])

        # Adding model 'Author'
        db.create_table('pugs_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('pugs', ['Author'])

        # Adding model 'PugAuthor'
        db.create_table('pugs_pugauthor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pug_authors', to=orm['pugs.Author'])),
            ('pug', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pug_authors', to=orm['pugs.Pug'])),
        ))
        db.send_create_signal('pugs', ['PugAuthor'])

        # Adding unique constraint on 'Pug', fields ['slug']
        db.create_unique('pugs_pug', ['slug'])

        # Adding unique constraint on 'Region', fields ['slug']
        db.create_unique('pugs_region', ['slug'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Region', fields ['slug']
        db.delete_unique('pugs_region', ['slug'])

        # Removing unique constraint on 'Pug', fields ['slug']
        db.delete_unique('pugs_pug', ['slug'])

        # Deleting model 'Post'
        db.delete_table('pugs_post')

        # Deleting model 'Author'
        db.delete_table('pugs_author')

        # Deleting model 'PugAuthor'
        db.delete_table('pugs_pugauthor')


    models = {
        'pugs.author': {
            'Meta': {'object_name': 'Author'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        },
        'pugs.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'countries'", 'to': "orm['pugs.Region']"})
        },
        'pugs.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': "orm['pugs.Author']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'pugs.pug': {
            'Meta': {'object_name': 'Pug'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pugs'", 'to': "orm['pugs.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'pugs.pugauthor': {
            'Meta': {'object_name': 'PugAuthor'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pug_authors'", 'to': "orm['pugs.Author']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pug': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pug_authors'", 'to': "orm['pugs.Pug']"})
        },
        'pugs.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['pugs']
