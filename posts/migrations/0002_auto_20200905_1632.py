# Generated by Django 3.1.1 on 2020-09-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_table',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
