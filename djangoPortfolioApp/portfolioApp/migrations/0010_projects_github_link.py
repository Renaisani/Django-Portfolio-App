# Generated by Django 4.1.7 on 2023-03-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0009_projectentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='github_link',
            field=models.CharField(default='', max_length=100),
        ),
    ]
