# Generated by Django 2.1.1 on 2018-09-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutModel', '0007_auto_20180926_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]
