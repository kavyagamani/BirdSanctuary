# Generated by Django 4.0 on 2023-07-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_generateticket_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generateticket',
            name='qrcode',
            field=models.ImageField(null=True, upload_to='docs/'),
        ),
    ]
