# Generated by Django 4.0 on 2023-06-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_pricemaster_visitor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeappointment',
            name='payment_status',
            field=models.CharField(max_length=60, null=True),
        ),
    ]