# Generated by Django 4.0 on 2022-04-03 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_users_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersfav',
            name='result1',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersfav',
            name='result2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersfav',
            name='result3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
