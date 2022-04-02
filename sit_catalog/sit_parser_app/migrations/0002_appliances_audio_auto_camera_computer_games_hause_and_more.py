# Generated by Django 4.0.3 on 2022-04-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sit_parser_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='AUDIO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='CAMERA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='COMPUTER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='GAMES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='HAUSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='PHONES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='POSSESIONS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='SPORT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='TOOLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='TOURISM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='TOYGOOFS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
        migrations.CreateModel(
            name='weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('price', models.PositiveIntegerField(verbose_name='цены')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.URLField(verbose_name='адреса сайта')),
            ],
        ),
    ]