# Generated by Django 2.2.7 on 2020-02-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0005_auto_20200208_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltests',
            name='referred_program',
            field=models.CharField(choices=[('ISM', 'ISM'), ('ISF', 'ISF'), ('MHFO', 'MHFO'), ('SUBAB', 'SUBAB'), ('DIAGNOSTIC', 'DIAGNOSTIC'), ('SEXOF-MH', 'SEXOF-MH'), ('SEXOF-SECURE', 'SEXOF-SECURE'), ('SEXOF', 'SEXOF'), ('ENHANCED', 'ENHANCED'), ('SECURE-MALE', 'SECURE-MALE'), ('SECURE-FEMALE', 'SECURE-FEMALE'), ('INDEPENDENT LIVING', 'INDEPENDENT LIVING')], db_column='referred_program', max_length=100),
        ),
    ]