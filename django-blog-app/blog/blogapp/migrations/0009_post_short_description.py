# Generated by Django 3.2.9 on 2022-02-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_category_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
