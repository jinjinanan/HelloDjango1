# Generated by Django 2.1.1 on 2018-09-27 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AboutModel', '0011_auto_20180927_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AboutModel.Comment'),
        ),
    ]
