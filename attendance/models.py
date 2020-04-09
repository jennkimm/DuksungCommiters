# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Repos(models.Model):
    repo_id = models.IntegerField(primary_key=True)
    reponame = models.CharField(max_length=150)
    owner = models.CharField(max_length=45)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        db_table = 'repos'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    userlogin = models.CharField(max_length=45)
    avartar_url = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'user'
