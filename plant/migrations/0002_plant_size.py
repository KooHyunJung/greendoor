# Generated by Django 4.0 on 2022-04-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plant", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plant",
            name="size",
            field=models.CharField(default="", max_length=1),
        ),
    ]