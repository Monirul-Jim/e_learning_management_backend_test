# Generated by Django 5.1.2 on 2024-10-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_alter_coursemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]
