from django.db import models


# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'
        ordering = ['sort']


class Portfolio(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    client = models.CharField(max_length=255, default='Default Name')
    name = models.CharField(max_length=255, default='Default Name')
    category = models.CharField(max_length=255)
    date = models.CharField(max_length=25)
    description = models.TextField()
    image_out = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    image_in = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'Портфоліо'
        verbose_name_plural = 'Портфоліо'
        ordering = ['sort']


class About(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    date = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'
        ordering = ['sort']


class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Працівник'
        verbose_name_plural = 'Працівники'
        ordering = ['sort']


class Clients(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clients/', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'
        ordering = ['sort']
