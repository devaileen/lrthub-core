# Generated by Django 2.0.7 on 2018-07-14 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180714_0445'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Disabilities',
            new_name='Disability',
        ),
    ]