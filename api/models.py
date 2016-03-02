from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, blank=True, default='')
    lastname = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('lastname',)