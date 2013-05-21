from django.db import models

class ContactSheet(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=512)

class TelephoneNumber(models.Model):
    number = models.CharField(max_length=128)
    sequence = models.SmallIntegerField()
    contactsheet = models.ForeignKey(ContactSheet)

class EmailAddress(models.Model):
    email = models.CharField(max_length=256)
    sequence = models.SmallIntegerField()
    contactsheet = models.ForeignKey(ContactSheet)

class PriceTier(models.Model):
    description = models.TextField()
    priceperweek = models.DecimalField(decimal_places=2, max_digits=7)
    numberofbeds = models.SmallIntegerField()

class Stage(models.Model):
    name = models.CharField(max_length=20)

class Booking(models.Model):
    datefrom = models.DateField()
    dateto = models.DateField()
    pricetier = models.ForeignKey(PriceTier)
    contactsheet = models.ForeignKey(ContactSheet)
    stage = models.ForeignKey(Stage)
    def weeknumbers(self):
        return self.datefrom.strftime("%U") + " - " + self.dateto.strftime("%U")
