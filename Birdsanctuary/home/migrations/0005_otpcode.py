# Generated by Django 4.0 on 2023-06-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_userlogin_password_alter_userlogin_utype'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
