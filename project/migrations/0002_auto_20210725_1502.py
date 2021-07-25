# Generated by Django 3.2.5 on 2021-07-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='massage',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='chronology',
            name='year',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.FileField(help_text='Upload your PDF file', upload_to='files/'),
        ),
    ]