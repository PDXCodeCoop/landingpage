from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Template(models.Model):
    active = models.BooleanField(default = False)
    header = models.CharField(max_length=100)
    subheader = models.CharField(max_length=300)
    about1 = models.TextField(max_length=300)
    about2 = models.TextField(max_length=300)
    def __unicode__(self):
        return "%s, Active:%s" % (self.header,self.active)
