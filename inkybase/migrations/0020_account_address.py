# Generated by Django 2.1.5 on 2019-04-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inkybase', '0019_auto_20190424_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
