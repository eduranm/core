# Generated by Django 4.2.7 on 2024-01-16 23:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_licensestatement_unique_together"),
        ("issue", "0002_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="tocsection",
            unique_together={("plain_text", "language")},
        ),
    ]
