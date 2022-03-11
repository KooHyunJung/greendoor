# Generated by Django 4.0 on 2022-03-11 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("plant", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("category", models.CharField(max_length=45)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("size", models.IntegerField()),
                ("info", models.CharField(max_length=500)),
                ("qty", models.IntegerField(default=0)),
                ("image", models.CharField(max_length=256)),
                ("image_tag", models.TextField(blank=True, null=True)),
                (
                    "plant_id",
                    models.ForeignKey(
                        db_column="plant_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="plant.plant",
                    ),
                ),
                (
                    "product_category_id",
                    models.ForeignKey(
                        db_column="product_category_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="product.productcategory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
