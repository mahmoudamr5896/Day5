# Generated by Django 5.0.2 on 2024-02-21 14:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0004_alter_team_manger"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="manger",
        ),
        migrations.DeleteModel(
            name="Eployee",
        ),
        migrations.DeleteModel(
            name="Team",
        ),
    ]
