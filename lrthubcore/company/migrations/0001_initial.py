# Generated by Django 2.0.7 on 2018-07-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
                ('cover_image', models.CharField(max_length=255)),
                ('contact_description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Company Profile Settings',
            },
        ),
    ]
