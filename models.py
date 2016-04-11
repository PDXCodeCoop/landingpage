from __future__ import unicode_literals
from easy_thumbnails.fields import ThumbnailerImageField

from django.db import models

# Create your models here.
class Template(models.Model):
    header_image = ThumbnailerImageField(upload_to='landingpage', blank=True, null=True)
    active = models.BooleanField(default = False)
    header = models.CharField(max_length=100)
    subheader = models.CharField(max_length=300)
    about1 = models.TextField(max_length=300)
    about2 = models.TextField(max_length=300)
    def __unicode__(self):
        return "%s, Active:%s" % (self.header,self.active)
