# Generated by Django 4.0 on 2022-03-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="info",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="size",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
