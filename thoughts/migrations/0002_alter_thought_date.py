# Generated by Django 4.1.2 on 2022-10-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thoughts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thought", name="date", field=models.CharField(max_length=100),
        ),
    ]
