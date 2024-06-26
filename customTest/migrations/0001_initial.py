# Generated by Django 5.0.4 on 2024-04-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msisdn', models.CharField(max_length=100)),
                ('imsi', models.CharField(max_length=100)),
                ('imei', models.CharField(max_length=100)),
                ('plan', models.CharField(max_length=100)),
                ('call_type', models.CharField(max_length=100)),
                ('corresp_type', models.CharField(max_length=100)),
                ('corresp_isdn', models.CharField(max_length=100)),
                ('duration', models.IntegerField(max_length=100)),
                ('date_time', models.DateTimeField(max_length=100)),
            ],
        ),
    ]
