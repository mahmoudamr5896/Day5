# Generated by Django 5.0.2 on 2024-02-21 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Epmloyee",
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
                ("name", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=50)),
                ("salary", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TeamLeader",
            fields=[
                (
                    "name",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                (
                    "manger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Manger_Name",
                        to="company.epmloyee",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="epmloyee",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="company.teamleader",
            ),
        ),
    ]
