# Generated by Django 3.1.4 on 2020-12-25 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0022_auto_20201224_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
