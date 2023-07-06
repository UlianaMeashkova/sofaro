# Generated by Django 4.1.7 on 2023-07-05 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0013_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Score",
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
                ("value", models.IntegerField()),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="scores",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]