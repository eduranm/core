# Generated by Django 4.2.7 on 2024-02-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0014_remove_officialjournal_issn_print_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subjectdescriptor",
            name="value",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
