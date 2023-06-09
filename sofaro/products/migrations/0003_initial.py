# Generated by Django 4.1.7 on 2023-05-22 15:54

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('color', models.CharField(choices=[('RED', 'Red'), ('GREEN', 'Green'), ('BLUE', 'Red')], default='RED', max_length=32)),
                ('price', models.DecimalField(decimal_places=5, default=Decimal('0'), max_digits=10)),
                ('price_usd', models.DecimalField(decimal_places=5, default=Decimal('0'), max_digits=10)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]
