# Generated by Django 5.1.2 on 2024-10-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0014_alter_ordermodel_payment_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='user',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(to='learning.cartitem')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderItemModel',
        ),
        migrations.DeleteModel(
            name='OrderModel',
        ),
    ]
