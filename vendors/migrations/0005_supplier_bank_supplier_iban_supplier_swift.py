# Generated by Django 5.1.2 on 2024-10-09 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_receiveditem_description_receiveditem_vendor_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='bank',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Bank'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='iban',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='IBAN'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='swift',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='SWIFT'),
        ),
    ]
