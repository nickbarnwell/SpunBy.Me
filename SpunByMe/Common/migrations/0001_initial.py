# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Song'
        db.create_table('common_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('swf_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('common', ['Song'])

        # Adding model 'SongQueue'
        db.create_table('common_songqueue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('common', ['SongQueue'])

        # Adding model 'QueueData'
        db.create_table('common_queuedata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Song'])),
            ('queue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.SongQueue'])),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('upvotes', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('downvotes', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('common', ['QueueData'])


    def backwards(self, orm):
        
        # Deleting model 'Song'
        db.delete_table('common_song')

        # Deleting model 'SongQueue'
        db.delete_table('common_songqueue')

        # Deleting model 'QueueData'
        db.delete_table('common_queuedata')


    models = {
        'common.queuedata': {
            'Meta': {'object_name': 'QueueData'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'downvotes': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'queue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.SongQueue']"}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Song']"}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'common.song': {
            'Meta': {'object_name': 'Song'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'swf_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'common.songqueue': {
            'Meta': {'object_name': 'SongQueue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['common.Song']", 'through': "orm['common.QueueData']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['common']
