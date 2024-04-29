from django.db import models
from django.core.validators import RegexValidator


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


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$',
                                 message="Number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    phone = models.CharField(validators=[phone_regex], max_length=15)
    email = models.EmailField()
    message = models.TextField()

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'
        ordering = ['-date_created']
