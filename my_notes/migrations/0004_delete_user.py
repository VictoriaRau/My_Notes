# Generated by Django 5.0.6 on 2024-06-09 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("my_notes", "0003_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
