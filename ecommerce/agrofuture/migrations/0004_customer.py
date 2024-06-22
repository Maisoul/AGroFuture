# Generated by Django 5.0.6 on 2024-06-21 21:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrofuture', '0003_rename_sellng_price_product_selling_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=10)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Kitusuru', 'Westlands'), ('Kilmani', 'Ngong-Road'), ('Karen', 'LAngata'), ('Kahawa West', 'Roysambu'), ('Kasarani', 'Kasarani-Low'), ('Kayole', 'Embakasi'), ('Utawala', 'Embakasi-Est'), ('Umoja', 'Ema west')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
