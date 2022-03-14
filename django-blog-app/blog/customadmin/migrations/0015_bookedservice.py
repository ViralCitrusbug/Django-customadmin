# Generated by Django 3.1.4 on 2020-12-17 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0014_auto_20201217_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('booking_charge', models.FloatField(blank=True, default=50, null=True)),
                ('service_date', models.DateField(blank=True, null=True)),
                ('service_time', models.TimeField(blank=True, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.service')),
                ('transaction_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.transactiondetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Purchased Product',
                'verbose_name_plural': 'Purchased Products',
                'ordering': ['-created_at'],
            },
        ),
    ]
