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
