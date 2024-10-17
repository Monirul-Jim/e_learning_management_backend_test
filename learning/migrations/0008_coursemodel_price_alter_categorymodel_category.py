# Generated by Django 5.1.2 on 2024-10-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_alter_coursemodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
