# Generated by Django 4.0 on 2022-03-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feed", "0003_feedbookmark_unique_user_feedbookmark_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="like_count",
            field=models.IntegerField(default=0),
        ),
    ]
