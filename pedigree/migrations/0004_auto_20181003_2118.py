# Generated by Django 2.1.2 on 2018-10-03 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedigree', '0003_goat_dor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goat',
            old_name='dor',
            new_name='date_of_registration',
        ),
    ]
