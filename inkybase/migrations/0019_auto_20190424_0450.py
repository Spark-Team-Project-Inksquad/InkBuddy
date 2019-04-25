# Generated by Django 2.1.5 on 2019-04-24 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inkybase', '0018_chat_chatmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='owner',
        ),
        migrations.AddField(
            model_name='chat',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='customer_chats', to='inkybase.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inkybase.Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='vendor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_chats', to='inkybase.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='from_account',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='messages_sent', to='inkybase.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='to_account',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='messages_recieved', to='inkybase.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inkybase.Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='customer_orders', to='inkybase.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='progression',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_orders', to='inkybase.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='vendor_spec',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inkybase.VendorSpec'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendorspec',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]