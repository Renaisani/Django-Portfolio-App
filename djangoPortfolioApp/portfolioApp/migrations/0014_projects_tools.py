# Generated by Django 4.1.7 on 2023-03-16 22:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0013_alter_contactentry_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='tools',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
    ]
