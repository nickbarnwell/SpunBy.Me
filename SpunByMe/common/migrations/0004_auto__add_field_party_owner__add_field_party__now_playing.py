# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Party.owner'
        db.add_column('common_party', 'owner', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['common.User']), keep_default=False)

        # Adding field 'Party._now_playing'
        db.add_column('common_party', '_now_playing', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Party.owner'
        db.delete_column('common_party', 'owner_id')

        # Deleting field 'Party._now_playing'
        db.delete_column('common_party', '_now_playing')


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
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'common.user': {
            'Meta': {'object_name': 'User'},
            'fb_username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['common']
