# Generated by Django 2.1.1 on 2018-09-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutModel', '0003_person_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='brithday',
            field=models.DateField(default='1993-11-26'),
        ),
    ]
