# Generated by Django 4.2.7 on 2023-12-21 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("collection", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("xmlsps", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PidProviderConfig",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                (
                    "pid_provider_api_post_xml",
                    models.TextField(
                        blank=True, null=True, verbose_name="XML Post URI"
                    ),
                ),
                (
                    "pid_provider_api_get_token",
                    models.TextField(
                        blank=True, null=True, verbose_name="Get Token URI"
                    ),
                ),
                (
                    "timeout",
                    models.IntegerField(blank=True, null=True, verbose_name="Timeout"),
                ),
                (
                    "api_username",
                    models.TextField(
                        blank=True, null=True, verbose_name="API Username"
                    ),
                ),
                (
                    "api_password",
                    models.TextField(
                        blank=True, null=True, verbose_name="API Password"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CollectionPidRequest",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                ("end_date", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "collection",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="collection.collection",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PidRequest",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        blank=True,
                        max_length=124,
                        null=True,
                        verbose_name="Request origin",
                    ),
                ),
                (
                    "result_type",
                    models.TextField(blank=True, null=True, verbose_name="Result type"),
                ),
                (
                    "result_msg",
                    models.TextField(
                        blank=True, null=True, verbose_name="Result message"
                    ),
                ),
                (
                    "detail",
                    models.JSONField(blank=True, null=True, verbose_name="Detail"),
                ),
                (
                    "origin_date",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Origin date"
                    ),
                ),
                (
                    "v3",
                    models.CharField(
                        blank=True, max_length=23, null=True, verbose_name="PID v3"
                    ),
                ),
                ("times", models.IntegerField(blank=True, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
                (
                    "xml_version",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="xmlsps.xmlversion",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["result_type"], name="pid_provide_result__f42960_idx"
                    ),
                    models.Index(fields=["v3"], name="pid_provide_v3_afbea7_idx"),
                    models.Index(fields=["times"], name="pid_provide_times_03e559_idx"),
                    models.Index(
                        fields=["detail"], name="pid_provide_detail_eeef1e_idx"
                    ),
                ],
            },
        ),
        migrations.CreateModel(
            name="PidProviderXML",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                (
                    "issn_electronic",
                    models.CharField(
                        blank=True, max_length=9, null=True, verbose_name="issn_epub"
                    ),
                ),
                (
                    "issn_print",
                    models.CharField(
                        blank=True, max_length=9, null=True, verbose_name="issn_ppub"
                    ),
                ),
                (
                    "pub_year",
                    models.CharField(
                        blank=True, max_length=4, null=True, verbose_name="pub_year"
                    ),
                ),
                (
                    "volume",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="volume"
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="number"
                    ),
                ),
                (
                    "suppl",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="suppl"
                    ),
                ),
                (
                    "pkg_name",
                    models.TextField(
                        blank=True, null=True, verbose_name="Package name"
                    ),
                ),
                (
                    "v3",
                    models.CharField(
                        blank=True, max_length=23, null=True, verbose_name="v3"
                    ),
                ),
                (
                    "v2",
                    models.CharField(
                        blank=True, max_length=23, null=True, verbose_name="v2"
                    ),
                ),
                (
                    "aop_pid",
                    models.CharField(
                        blank=True, max_length=23, null=True, verbose_name="AOP PID"
                    ),
                ),
                (
                    "elocation_id",
                    models.TextField(
                        blank=True, null=True, verbose_name="elocation id"
                    ),
                ),
                (
                    "fpage",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="fpage"
                    ),
                ),
                (
                    "fpage_seq",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="fpage_seq"
                    ),
                ),
                (
                    "lpage",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="lpage"
                    ),
                ),
                (
                    "article_pub_year",
                    models.CharField(
                        blank=True,
                        max_length=4,
                        null=True,
                        verbose_name="Document Publication Year",
                    ),
                ),
                (
                    "main_toc_section",
                    models.TextField(
                        blank=True, null=True, verbose_name="main_toc_section"
                    ),
                ),
                (
                    "main_doi",
                    models.TextField(blank=True, null=True, verbose_name="DOI"),
                ),
                (
                    "z_article_titles_texts",
                    models.CharField(
                        blank=True,
                        max_length=64,
                        null=True,
                        verbose_name="article_titles_texts",
                    ),
                ),
                (
                    "z_surnames",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="surnames"
                    ),
                ),
                (
                    "z_collab",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="collab"
                    ),
                ),
                (
                    "z_links",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="links"
                    ),
                ),
                (
                    "z_partial_body",
                    models.CharField(
                        blank=True,
                        max_length=64,
                        null=True,
                        verbose_name="partial_body",
                    ),
                ),
                (
                    "origin_date",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Origin date"
                    ),
                ),
                (
                    "website_publication_date",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Website publication date",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "current_version",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="xmlsps.xmlversion",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["pkg_name"], name="pid_provide_pkg_nam_009b25_idx"
                    ),
                    models.Index(fields=["v3"], name="pid_provide_v3_e61beb_idx"),
                    models.Index(
                        fields=["issn_electronic"],
                        name="pid_provide_issn_el_2f7625_idx",
                    ),
                    models.Index(
                        fields=["issn_print"], name="pid_provide_issn_pr_988775_idx"
                    ),
                    models.Index(
                        fields=["pub_year"], name="pid_provide_pub_yea_2cf929_idx"
                    ),
                    models.Index(
                        fields=["volume"], name="pid_provide_volume_6abc53_idx"
                    ),
                    models.Index(
                        fields=["number"], name="pid_provide_number_a56cd7_idx"
                    ),
                    models.Index(fields=["suppl"], name="pid_provide_suppl_b4294e_idx"),
                    models.Index(
                        fields=["elocation_id"], name="pid_provide_elocati_088a9b_idx"
                    ),
                    models.Index(fields=["fpage"], name="pid_provide_fpage_aa4aa3_idx"),
                    models.Index(
                        fields=["fpage_seq"], name="pid_provide_fpage_s_cd49cb_idx"
                    ),
                    models.Index(fields=["lpage"], name="pid_provide_lpage_7a7852_idx"),
                    models.Index(
                        fields=["article_pub_year"],
                        name="pid_provide_article_e25491_idx",
                    ),
                    models.Index(
                        fields=["main_doi"], name="pid_provide_main_do_7fb3c9_idx"
                    ),
                    models.Index(
                        fields=["z_article_titles_texts"],
                        name="pid_provide_z_artic_a6a417_idx",
                    ),
                    models.Index(
                        fields=["z_surnames"], name="pid_provide_z_surna_2f3ee3_idx"
                    ),
                    models.Index(
                        fields=["z_collab"], name="pid_provide_z_colla_c14f41_idx"
                    ),
                    models.Index(
                        fields=["z_links"], name="pid_provide_z_links_ed20b4_idx"
                    ),
                    models.Index(
                        fields=["z_partial_body"], name="pid_provide_z_parti_6ab872_idx"
                    ),
                ],
            },
        ),
        migrations.CreateModel(
            name="PidChange",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                (
                    "pkg_name",
                    models.TextField(
                        blank=True, null=True, verbose_name="Package name"
                    ),
                ),
                (
                    "pid_type",
                    models.CharField(
                        blank=True, max_length=23, null=True, verbose_name="PID type"
                    ),
                ),
                (
                    "pid_in_xml",
                    models.CharField(
                        blank=True,
                        max_length=23,
                        null=True,
                        verbose_name="PID pid_in_xml",
                    ),
                ),
                (
                    "pid_assigned",
                    models.CharField(
                        blank=True,
                        max_length=23,
                        null=True,
                        verbose_name="PID assigned",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
                (
                    "version",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="xmlsps.xmlversion",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["pid_in_xml"], name="pid_provide_pid_in__da2270_idx"
                    ),
                    models.Index(
                        fields=["pid_assigned"], name="pid_provide_pid_ass_a06263_idx"
                    ),
                    models.Index(
                        fields=["pid_type"], name="pid_provide_pid_typ_cb60fc_idx"
                    ),
                    models.Index(
                        fields=["version"], name="pid_provide_version_f0e2c3_idx"
                    ),
                ],
            },
        ),
    ]
