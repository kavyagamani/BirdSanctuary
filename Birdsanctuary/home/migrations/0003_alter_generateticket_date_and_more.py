# Generated by Django 4.0 on 2023-06-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_takeappointment_amount_per_member_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generateticket',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='takeappointment',
            name='appointment_date',
            field=models.DateField(null=True),
        ),
    ]
