# Generated by Django 4.2.7 on 2023-12-21 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("editorialboard", "0002_initial"),
        ("journal", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="editorialboard",
            name="journal",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="journal.journal",
            ),
        ),
        migrations.AddField(
            model_name="editorialboard",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(class)s_last_mod_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Updater",
            ),
        ),
        migrations.AddIndex(
            model_name="rolemodel",
            index=models.Index(
                fields=["declared_role"], name="editorialbo_declare_bd3ba2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="rolemodel",
            index=models.Index(
                fields=["std_role"], name="editorialbo_std_rol_b91ae3_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="rolemodel",
            unique_together={("declared_role", "std_role")},
        ),
        migrations.AlterUniqueTogether(
            name="editorialboardmember",
            unique_together={("editorial_board", "researcher", "role")},
        ),
        migrations.AddIndex(
            model_name="editorialboard",
            index=models.Index(
                fields=["initial_year"], name="editorialbo_initial_011435_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="editorialboard",
            index=models.Index(
                fields=["final_year"], name="editorialbo_final_y_cb55bc_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="editorialboard",
            unique_together={("journal", "initial_year", "final_year")},
        ),
    ]
