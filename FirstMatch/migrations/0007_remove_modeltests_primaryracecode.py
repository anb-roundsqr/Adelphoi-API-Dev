# Generated by Django 2.2.7 on 2020-02-14 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0006_auto_20200209_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeltests',
            name='primaryRaceCode',
        ),
    ]