# Generated by Django 2.1.1 on 2018-09-26 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AboutModel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
    ]