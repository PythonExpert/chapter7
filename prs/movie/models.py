# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Genres(models.Model):
    movieid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=False, primary_key=True)
    genre = models.CharField(max_length=50, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'genres'


class Movies(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=False, primary_key=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    imdbid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spanishtitle = models.CharField(max_length=150, blank=True, null=True)
    imdbpictureurl = models.CharField(max_length=250, blank=True, null=True)
    year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtid = models.CharField(max_length=150, blank=True, null=True)
    rtallcriticsrating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtallcriticsnumreviews = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtallcriticsnumfresh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtallcriticsnumrotten = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtallcriticsscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rttopcriticsrating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rttopcriticsnumreviews = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rttopcriticsnumfresh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rttopcriticsnumrotten = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rttopcriticsscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtaudiencerating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtaudiencenumratings = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtaudiencescore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rtpictureurl = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'movies'

    