# Generated by Django 2.2.12 on 2020-05-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0014_auto_20200502_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adelphoi_mapping',
            name='default_level_facility',
            field=models.BooleanField(db_column='default_level_facility', default=True),
        ),
    ]
