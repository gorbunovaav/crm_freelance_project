# Generated by Django 5.2.4 on 2025-07-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0003_rename_prority_lead_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="converted_to_client",
            field=models.BooleanField(default=False),
        ),
    ]
