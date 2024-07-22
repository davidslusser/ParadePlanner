# Generated by Django 5.0.7 on 2024-07-22 00:21

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("street_address", models.CharField(max_length=255)),
                ("address_extra", models.CharField(blank=True, max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("postal_code", models.CharField(max_length=20)),
                (
                    "address_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Corporate", "Corporate"),
                            ("Branch", "Branch"),
                            ("Home", "Home"),
                            ("Other", "Other"),
                        ],
                        max_length=16,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AwardType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32, unique=True)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("enabled", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32, unique=True)),
                ("label", models.CharField(max_length=2, unique=True)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("enabled", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EmailAddress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "email_address_type",
                    models.CharField(
                        blank=True,
                        choices=[("Direct", "Direct"), ("Work", "Work"), ("Personal", "Personal"), ("Other", "Other")],
                        max_length=16,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=32)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("url", models.URLField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Parade",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(blank=True, max_length=64)),
                (
                    "year",
                    models.IntegerField(
                        help_text="Enter a valid year",
                        validators=[
                            django.core.validators.MinValueValidator(2000),
                            django.core.validators.MaxValueValidator(2029),
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("number", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                (
                    "phone_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Direct", "Direct"),
                            ("Fax", "Fax"),
                            ("Home", "Home"),
                            ("Mobile", "Mobile"),
                            ("Office", "Office"),
                            ("Other", "Other"),
                        ],
                        max_length=16,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Division",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("label", models.CharField(max_length=2)),
                ("name", models.CharField(max_length=64)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("enabled", models.BooleanField(default=True)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="parademgr.category")),
            ],
            options={
                "unique_together": {("category", "name")},
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("addresses", models.ManyToManyField(blank=True, to="parademgr.address")),
                ("emails", models.ManyToManyField(blank=True, to="parademgr.emailaddress")),
                ("links", models.ManyToManyField(blank=True, to="parademgr.link")),
                ("phone_numbers", models.ManyToManyField(blank=True, to="parademgr.phonenumber")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=64, unique=True)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("addresses", models.ManyToManyField(blank=True, to="parademgr.address")),
                ("contacts", models.ManyToManyField(blank=True, to="parademgr.contact")),
                ("emails", models.ManyToManyField(blank=True, to="parademgr.emailaddress")),
                ("links", models.ManyToManyField(blank=True, to="parademgr.link")),
                ("phone_numbers", models.ManyToManyField(blank=True, to="parademgr.phonenumber")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("entry", models.IntegerField(blank=True, null=True)),
                ("street", models.CharField(max_length=32, null=True)),
                ("march_order", models.IntegerField(blank=True, null=True)),
                ("division", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="parademgr.division")),
                (
                    "organization",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="parademgr.organization"),
                ),
                ("parade", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="parademgr.parade")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Award",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=32)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("amount", models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                (
                    "award_type",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="parademgr.awardtype"),
                ),
                (
                    "division",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="parademgr.division"
                    ),
                ),
                (
                    "winner",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="parademgr.participant"
                    ),
                ),
            ],
            options={
                "unique_together": {("division", "name")},
            },
        ),
    ]
