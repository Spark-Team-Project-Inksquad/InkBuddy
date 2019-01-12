# Generated by Django 2.1.5 on 2019-01-12 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inkybase', '0010_vendorreview_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='printing_medium',
        ),
        migrations.AddField(
            model_name='documenttype',
            name='printing_medium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inkybase.PrintingMedium'),
        ),
    ]
