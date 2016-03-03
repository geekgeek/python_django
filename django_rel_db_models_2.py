from __future__ import unicode_literals

from django.db import models

class Dude(models.Model):
    name = models.CharField(max_length=140)
    
    def __unicode__(self):
        return self.name

class PhoneNumber(models.Model):
    dude = models.ForeignKey(Dude)
    number = models.CharField(max_length=140)
    
    def __unicode__(self):
        return self.dude.name
