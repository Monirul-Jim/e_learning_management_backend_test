# Generated by Django 5.1.2 on 2024-10-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_rename_category_categorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]