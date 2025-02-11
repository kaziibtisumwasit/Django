# Generated by Django 5.1.5 on 2025-02-04 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('author', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='author.author')),
            ],
        ),
    ]
