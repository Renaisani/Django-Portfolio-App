# Generated by Django 4.1.7 on 2023-03-07 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0008_delete_projectentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=255)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(default='', max_length=1000)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.projects')),
            ],
        ),
    ]