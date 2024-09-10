# Generated by Django 5.1 on 2024-08-23 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("master_price", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productssodimac",
            old_name="sku_sodimac",
            new_name="publication",
        ),
        migrations.RemoveField(
            model_name="productsmeli",
            name="publications_meli",
        ),
        migrations.RemoveField(
            model_name="productssodimac",
            name="publications_sodimac",
        ),
        migrations.AddField(
            model_name="productsmeli",
            name="main_product",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="master_price.mainproducts",
                verbose_name="main_product",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productsmeli",
            name="publication",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="productssodimac",
            name="main_product",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="master_price.mainproducts",
                verbose_name="main_product",
            ),
            preserve_default=False,
        ),
    ]
