# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'User', fields ['fb_username']
        db.create_unique('common_user', ['fb_username'])

        # Adding field 'Song.albumart_url'
        db.add_column('common_song', 'albumart_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Removing unique constraint on 'User', fields ['fb_username']
        db.delete_unique('common_user', ['fb_username'])

        # Deleting field 'Song.albumart_url'
        db.delete_column('common_song', 'albumart_url')


    models = {
        'common.party': {
            'Meta': {'object_name': 'Party'},
            '_now_playing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.User']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['common.Song']", 'through': "orm['common.QueueData']", 'symmetrical': 'False'})
        },
        'common.queuedata': {
            'Meta': {'object_name': 'QueueData'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'downvotes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Party']"}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Song']"}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'common.song': {
            'Meta': {'object_name': 'Song'},
            'albumart_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'common.user': {
            'Meta': {'object_name': 'User'},
            'fb_username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['common']
