# Generated by Django 3.1.4 on 2020-12-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0018_auto_20201221_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
