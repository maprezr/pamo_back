# Generated by Django 5.1 on 2024-08-23 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MainProducts",
            fields=[
                (
                    "id_variantShopi",
                    models.CharField(max_length=300, primary_key=True, serialize=False),
                ),
                ("id_product", models.CharField(max_length=20)),
                ("title", models.CharField(blank=True, max_length=300, null=True)),
                ("tags", models.CharField(blank=True, max_length=500, null=True)),
                ("vendor", models.CharField(blank=True, max_length=100, null=True)),
                ("status", models.CharField(blank=True, max_length=100, null=True)),
                ("price", models.FloatField(blank=True, default=0, null=True)),
                (
                    "compare_at_price",
                    models.FloatField(blank=True, default=0, null=True),
                ),
                ("sku", models.CharField(blank=True, max_length=100, null=True)),
                ("barcode", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "inventory_quantity",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("cursor", models.CharField(blank=True, max_length=80, null=True)),
                ("margen", models.FloatField(blank=True, default=0, null=True)),
                ("costo", models.FloatField(blank=True, default=0, null=True)),
                (
                    "margen_comparacion_db",
                    models.FloatField(blank=True, default=0, null=True),
                ),
                ("kit", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ProductsMeli",
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
                (
                    "pricePublication",
                    models.FloatField(blank=True, default=0, null=True),
                ),
                ("taxes", models.FloatField(blank=True, default=0, null=True)),
                ("margen", models.SmallIntegerField(default=0)),
                (
                    "publications_meli",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="master_price.mainproducts",
                        verbose_name="publications_meli",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductsSodimac",
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
                (
                    "sku_sodimac",
                    models.CharField(blank=True, max_length=50, null=True, unique=True),
                ),
                (
                    "ean",
                    models.CharField(blank=True, max_length=15, null=True, unique=True),
                ),
                ("stock", models.IntegerField(blank=True, default=0, null=True)),
                ("stock_sodi", models.IntegerField(blank=True, default=0, null=True)),
                ("margen", models.SmallIntegerField(default=0)),
                (
                    "publications_sodimac",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="master_price.mainproducts",
                        verbose_name="publications_sodimac",
                    ),
                ),
            ],
        ),
    ]
