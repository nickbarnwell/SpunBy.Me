# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Song.swf_url'
        db.delete_column('common_song', 'swf_url')

        # Adding field 'Song.video_id'
        db.add_column('common_song', 'video_id', self.gf('django.db.models.fields.CharField')(default='_OBlgSz8sSM', max_length=64), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Song.swf_url'
        db.add_column('common_song', 'swf_url', self.gf('django.db.models.fields.URLField')(default='not a url', max_length=200), keep_default=False)

        # Deleting field 'Song.video_id'
        db.delete_column('common_song', 'video_id')


    models = {
        'common.party': {
            'Meta': {'object_name': 'Party'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
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
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'common.user': {
            'Meta': {'object_name': 'User'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['common']
