# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table(u'feedback_form_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'feedback_form', ['Employee'])

        # Adding model 'Feedback'
        db.create_table(u'feedback_form_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback_form.Employee'])),
            ('feedback', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'feedback_form', ['Feedback'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'feedback_form_employee')

        # Deleting model 'Feedback'
        db.delete_table(u'feedback_form_feedback')


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
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback_form.Employee']"})
        }
    }

    complete_apps = ['feedback_form']