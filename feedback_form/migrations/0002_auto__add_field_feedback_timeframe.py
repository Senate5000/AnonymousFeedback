# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Feedback.timeframe'
        db.add_column(u'feedback_form_feedback', 'timeframe',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 6, 17, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Feedback.timeframe'
        db.delete_column(u'feedback_form_feedback', 'timeframe')


    models = {
        u'feedback_form.employee': {
            'Meta': {'object_name': 'Employee'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'feedback_form.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'feedback': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback_form.Employee']"}),
            'timeframe': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['feedback_form']