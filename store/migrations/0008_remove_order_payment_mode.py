# Generated by Django 4.1.6 on 2023-07-12 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_payment_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_mode',
        ),
    ]
