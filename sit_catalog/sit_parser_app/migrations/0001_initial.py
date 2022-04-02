# Generated by Django 4.0.3 on 2022-04-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SITdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
    ]
