# Generated by Django 4.0 on 2023-06-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_generateticket_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='password',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='utype',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
