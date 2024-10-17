# Generated by Django 5.1.2 on 2024-10-17 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0009_remove_coursemodel_category_coursemodel_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='categories',
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='price',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.categorymodel'),
        ),
    ]