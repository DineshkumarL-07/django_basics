# Generated by Django 5.1.2 on 2024-11-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("firstName", models.CharField(max_length=50)),
                ("lastName", models.CharField(max_length=50)),
                ("emailID", models.EmailField(max_length=50, unique=True)),
                ("passWord", models.CharField(max_length=20)),
                ("photo", models.ImageField(upload_to="images")),
                ("phoneNo", models.CharField(blank=True, max_length=10)),
                ("userCreatedAt", models.DateTimeField(auto_now_add=True)),
                ("userUpdatedAt", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
