# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Action(models.Model):
    act_id = models.CharField(primary_key=True, max_length=20)
    act_consumer = models.ForeignKey('User', models.DO_NOTHING, db_column='act_consumer')
    act_type = models.IntegerField()
    act_date = models.CharField(max_length=45)
    act_pro = models.ForeignKey('Products', models.DO_NOTHING, db_column='act_pro')

    class Meta:
        managed = False
        db_table = 'action'


class Class(models.Model):
    cla_id = models.CharField(primary_key=True, max_length=20)
    cla_date = models.CharField(max_length=45)
    cla_kind = models.CharField(max_length=45)
    cla_yeild = models.CharField(max_length=45)
    cla_per = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'class'



class Gdp(models.Model):

    gdp_id = models.CharField(primary_key=True, max_length=20)
    gdp_date = models.CharField(max_length=45)
    gdp_mount = models.CharField(max_length=45)
    gdp_all = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gdp'

class Price(models.Model):
    pri_id = models.CharField(primary_key=True, max_length=20)
    pri_place = models.CharField(max_length=45)
    pri_kind = models.CharField(max_length=45)
    pri_name = models.CharField(max_length=45)
    pri_date = models.CharField(max_length=45)
    pri_price = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'price'


class Products(models.Model):
    pro_id = models.CharField(primary_key=True, max_length=20)
    pro_name = models.CharField(max_length=45)
    pro_type = models.CharField(max_length=45)
    pro_price = models.DecimalField(max_digits=5, decimal_places=1)
    pro_origin = models.CharField(max_length=45)
    pro_des = models.CharField(max_length=45)
    pro_img = models.CharField(max_length=45, blank=True, null=True)
    pro_store = models.ForeignKey('User', models.DO_NOTHING, db_column='pro_store')
    pro_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Purchase(models.Model):
    pur_id = models.CharField(primary_key=True, max_length=20)
    pur_consumer = models.ForeignKey('User', models.DO_NOTHING, db_column='pur_consumer')
    pur_product = models.ForeignKey(Products, models.DO_NOTHING, db_column='pur_product')
    pur_quantity = models.CharField(max_length=45)
    pur_date = models.CharField(max_length=45)
    pur_price = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'purchase'


class User(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)
    user_pwd = models.CharField(max_length=45)
    user_type = models.IntegerField()
    user_address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Weather(models.Model):
    wea_id = models.CharField(primary_key=True, max_length=20)
    wea_temp_max = models.IntegerField()
    wea_temp_min = models.IntegerField()
    wea_state = models.IntegerField()
    wea_place = models.CharField(max_length=45)
    wea_date = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'weather'


class Yield(models.Model):
    yie_id = models.CharField(primary_key=True, max_length=20)
    yie_place = models.CharField(max_length=45)
    yie_kind = models.CharField(max_length=45)
    yie_yield = models.CharField(max_length=45)
    yie_date = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'yield'
