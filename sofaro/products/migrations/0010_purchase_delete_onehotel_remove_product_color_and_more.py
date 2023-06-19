# Generated by Django 4.1.7 on 2023-06-14 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0009_onehotel_remove_product_color_purchase"),
    ]

    operations = [
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.DeleteModel(
            name="OneHotel",
        ),
        migrations.RemoveField(
            model_name="product",
            name="color",
        ),
        migrations.AlterField(
            model_name="hotels",
            name="country",
            field=models.CharField(
                choices=[
                    ("Турция", "ТУРЦИЯ"),
                    ("ОАЭ", "ОАЭ"),
                    ("Египет", "ЕГИПЕТ"),
                    ("Греция", "ГРЕЦИЯ"),
                ],
                default="Турция",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="country",
            field=models.CharField(
                choices=[
                    ("Турция", "ТУРЦИЯ"),
                    ("ОАЭ", "ОАЭ"),
                    ("Египет", "ЕГИПЕТ"),
                    ("Греция", "ГРЕЦИЯ"),
                ],
                default="Турция",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="purchase",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchases",
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="purchase",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchases",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
