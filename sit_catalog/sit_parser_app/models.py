from django.contrib.auth.models import User
from django.db import models
from bs4 import BeautifulSoup
import sqlite3
import requests


class SITdb(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class Phone(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class POSSESIONS(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class COMPUTER(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class CAMERA(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class CAMERA(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class AUDIO(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class GAMES(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class TV(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class appliances(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class appliances(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class weather(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class HOUSE(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class TOYGOOFS(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class auto(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class TOOLS(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class TOURISM(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

class SPORT(models.Model):
    title = models.TextField(
        verbose_name='название',
    )
    price = models.PositiveIntegerField(
        verbose_name='цены',
    )
    description = models.TextField(
        verbose_name='описание',
    )
    url = models.URLField(
        verbose_name='адреса сайта',
    )

















