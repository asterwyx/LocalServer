# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Table1351379(models.Model):
    id = models.BigAutoField(primary_key=True)
    aid = models.BigIntegerField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    duration = models.TimeField()
    num_of_coins = models.BigIntegerField()
    num_of_likes = models.BigIntegerField()
    num_of_favorites = models.BigIntegerField()
    num_of_replies = models.BigIntegerField()
    num_of_shares = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'table_1351379'


class Table16794231(models.Model):
    id = models.BigAutoField(primary_key=True)
    aid = models.BigIntegerField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    duration = models.TimeField()
    num_of_coins = models.BigIntegerField()
    num_of_likes = models.BigIntegerField()
    num_of_favorites = models.BigIntegerField()
    num_of_replies = models.BigIntegerField()
    num_of_shares = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'table_16794231'


class Table23172676(models.Model):
    id = models.BigAutoField(primary_key=True)
    aid = models.BigIntegerField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    duration = models.TimeField()
    num_of_coins = models.BigIntegerField()
    num_of_likes = models.BigIntegerField()
    num_of_favorites = models.BigIntegerField()
    num_of_replies = models.BigIntegerField()
    num_of_shares = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'table_23172676'


class Table6574487(models.Model):
    id = models.BigAutoField(primary_key=True)
    aid = models.BigIntegerField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    duration = models.TimeField()
    num_of_coins = models.BigIntegerField()
    num_of_likes = models.BigIntegerField()
    num_of_favorites = models.BigIntegerField()
    num_of_replies = models.BigIntegerField()
    num_of_shares = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'table_6574487'


class Upname(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.BigIntegerField()
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'upname'
