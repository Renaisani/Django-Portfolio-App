# Generated by Django 4.1.7 on 2023-03-14 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0011_contactentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactentry',
            name='company',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
