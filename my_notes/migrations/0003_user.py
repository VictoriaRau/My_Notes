# Generated by Django 5.0.6 on 2024-06-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_notes", "0002_rename_created_by_task_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=100)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]