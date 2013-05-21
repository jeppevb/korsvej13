# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactSheet'
        db.create_table('booking_contactsheet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('booking', ['ContactSheet'])

        # Adding model 'TelephoneNumber'
        db.create_table('booking_telephonenumber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('sequence', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('contactsheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.ContactSheet'])),
        ))
        db.send_create_signal('booking', ['TelephoneNumber'])

        # Adding model 'EmailAddress'
        db.create_table('booking_emailaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sequence', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('contactsheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.ContactSheet'])),
        ))
        db.send_create_signal('booking', ['EmailAddress'])

        # Adding model 'PriceTier'
        db.create_table('booking_pricetier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('priceperweek', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('numberofbeds', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('booking', ['PriceTier'])

        # Adding model 'Stage'
        db.create_table('booking_stage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('booking', ['Stage'])

        # Adding model 'Booking'
        db.create_table('booking_booking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datefrom', self.gf('django.db.models.fields.DateField')()),
            ('dateto', self.gf('django.db.models.fields.DateField')()),
            ('pricetier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.PriceTier'])),
            ('contactsheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.ContactSheet'])),
            ('stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.Stage'])),
        ))
        db.send_create_signal('booking', ['Booking'])


    def backwards(self, orm):
        # Deleting model 'ContactSheet'
        db.delete_table('booking_contactsheet')

        # Deleting model 'TelephoneNumber'
        db.delete_table('booking_telephonenumber')

        # Deleting model 'EmailAddress'
        db.delete_table('booking_emailaddress')

        # Deleting model 'PriceTier'
        db.delete_table('booking_pricetier')

        # Deleting model 'Stage'
        db.delete_table('booking_stage')

        # Deleting model 'Booking'
        db.delete_table('booking_booking')


    models = {
        'booking.booking': {
            'Meta': {'object_name': 'Booking'},
            'contactsheet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.ContactSheet']"}),
            'datefrom': ('django.db.models.fields.DateField', [], {}),
            'dateto': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pricetier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.PriceTier']"}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.Stage']"})
        },
        'booking.contactsheet': {
            'Meta': {'object_name': 'ContactSheet'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'booking.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'contactsheet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.ContactSheet']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'booking.pricetier': {
            'Meta': {'object_name': 'PriceTier'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numberofbeds': ('django.db.models.fields.SmallIntegerField', [], {}),
            'priceperweek': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        },
        'booking.stage': {
            'Meta': {'object_name': 'Stage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'booking.telephonenumber': {
            'Meta': {'object_name': 'TelephoneNumber'},
            'contactsheet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.ContactSheet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sequence': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['booking']