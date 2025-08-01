# Generated by Django 5.2.4 on 2025-07-24 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0004_lead_converted_to_client"),
        ("team", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="team",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="leads",
                to="team.team",
            ),
            preserve_default=False,
        ),
    ]
