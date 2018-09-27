# Generated by Django 2.1.1 on 2018-09-27 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AboutModel', '0010_auto_20180927_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AboutModel.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
