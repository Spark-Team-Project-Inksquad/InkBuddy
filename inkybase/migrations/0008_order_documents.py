# Generated by Django 2.1.5 on 2019-01-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inkybase', '0007_auto_20190110_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='documents',
            field=models.ManyToManyField(to='inkybase.Document'),
        ),
    ]
