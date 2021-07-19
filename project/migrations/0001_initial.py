# Generated by Django 3.2.5 on 2021-07-17 08:41

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('massage', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_photo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Galleries',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=650)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('gallery', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('gallery', ckeditor_uploader.fields.RichTextUploadingField()),
                ('start_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('region', models.CharField(choices=[('Чуй', 'Чуй'), ('Бишкек', 'Бишкек'), ('Иссык-Куль', 'Иссык-Куль'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Ош', 'Ош'), ('Баткен', 'Баткен'), ('Жалал-Абад', 'Жалал-Абад')], max_length=200)),
                ('project_number', models.IntegerField()),
                ('is_finished', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('Альянс', 'Альянсы для устойчивого развития'), ('Гос', 'Государственное управление, мир и безопасность'), ('Парт', 'Партнерство в сфере миграции'), ('Цифр', 'Цифровизация наука, технологии и инновации'), ('Зелен', 'Зеленая экономика')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['created'],
            },
        ),
    ]