# Generated by Django 5.1.2 on 2024-10-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_session_id', models.CharField(max_length=255, unique=True)),
                ('amount_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]