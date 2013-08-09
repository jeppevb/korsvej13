# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactSheet'
        db.create_table(u'booking_contactsheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'booking', ['ContactSheet'])

        # Adding model 'TelephoneNumber'
        db.create_table(u'booking_telephonenumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('sequence', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('contactsheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.ContactSheet'])),
        ))
        db.send_create_signal(u'booking', ['TelephoneNumber'])

        # Adding model 'EmailAddress'
        db.create_table(u'booking_emailaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sequence', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('contactsheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.ContactSheet'])),
        ))
        db.send_create_signal(u'booking', ['EmailAddress'])

        # Adding model 'PriceTier'
        db.create_table(u'booking_pricetier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('priceperweek', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('numberofbeds', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'booking', ['PriceTier'])

        # Adding model 'Stage'
        db.create_table(u'booking_stage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'booking', ['Stage'])

        # Adding model 'Booking'
        db.create_table(u'booking_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pricetier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.PriceTier'])),
            ('contactsheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.ContactSheet'])),
            ('stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.Stage'])),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('firstday', self.gf('django.db.models.fields.DateField')()),
            ('lastday', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'booking', ['Booking'])


    def backwards(self, orm):
        # Deleting model 'ContactSheet'
        db.delete_table(u'booking_contactsheet')

        # Deleting model 'TelephoneNumber'
        db.delete_table(u'booking_telephonenumber')

        # Deleting model 'EmailAddress'
        db.delete_table(u'booking_emailaddress')

        # Deleting model 'PriceTier'
        db.delete_table(u'booking_pricetier')

        # Deleting model 'Stage'
        db.delete_table(u'booking_stage')

        # Deleting model 'Booking'
        db.delete_table(u'booking_booking')


    models = {
        u'booking.booking': {
            'Meta': {'object_name': 'Booking'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contactsheet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.ContactSheet']"}),
            'firstday': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastday': ('django.db.models.fields.DateField', [], {}),
            'pricetier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.PriceTier']"}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.Stage']"})
        },
        u'booking.contactsheet': {
            'Meta': {'object_name': 'ContactSheet'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'booking.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'contactsheet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.ContactSheet']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'booking.pricetier': {
            'Meta': {'object_name': 'PriceTier'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numberofbeds': ('django.db.models.fields.SmallIntegerField', [], {}),
            'priceperweek': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        },
        u'booking.stage': {
            'Meta': {'object_name': 'Stage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'booking.telephonenumber': {
            'Meta': {'object_name': 'TelephoneNumber'},
            'contactsheet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['booking.ContactSheet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sequence': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['booking']