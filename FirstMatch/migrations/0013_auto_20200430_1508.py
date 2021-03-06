# Generated by Django 2.2.12 on 2020-04-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstMatch', '0012_auto_20200324_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltests',
            name='referred_program',
            field=models.CharField(choices=[('ISM', 'ISM'), ('ISF', 'ISF'), ('MHFO', 'MHFO'), ('SUBAB', 'SUBAB'), ('SEXOF-MH', 'SEXOF-MH'), ('SEXOF-SECURE', 'SEXOF-SECURE'), ('SEXOF', 'SEXOF'), ('SECURE-MALE', 'SECURE-MALE'), ('SECURE-FEMALE', 'SECURE-FEMALE'), ('INDEPENDENT LIVING', 'Independent Living'), ('Transitional Living', 'Transitional Living')], db_column='referred_program', default=1, max_length=100),
            preserve_default=False,
        ),
    ]
