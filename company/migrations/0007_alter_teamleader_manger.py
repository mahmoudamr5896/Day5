# Generated by Django 5.0.2 on 2024-02-21 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0006_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teamleader",
            name="manger",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="company.epmloyee"
            ),
        ),
    ]
