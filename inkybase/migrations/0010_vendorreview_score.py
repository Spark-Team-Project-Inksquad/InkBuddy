# Generated by Django 2.1.5 on 2019-01-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inkybase', '0009_offerspec'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorreview',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
