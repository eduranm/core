# Generated by Django 4.1.10 on 2023-09-20 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_license_core_licens_url_e7d241_idx_and_more"),
        ("journal", "0007_journal_acronym_letters_journal_center_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="journal",
            name="use_license",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.license",
            ),
        ),
    ]
