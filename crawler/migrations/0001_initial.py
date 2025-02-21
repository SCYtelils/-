# Generated by Django 4.1 on 2023-11-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnalysisResult",
            fields=[
                (
                    "timestamp",
                    models.TextField(blank=True, primary_key=True, serialize=False),
                ),
                ("year", models.IntegerField(blank=True, null=True)),
                (
                    "actual_value_field",
                    models.FloatField(blank=True, db_column="actual_value ", null=True),
                ),
                (
                    "predicted_value_field",
                    models.FloatField(
                        blank=True, db_column="predicted_value ", null=True
                    ),
                ),
                ("prediction_error", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "analysis_result",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Data",
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
                ("region", models.TextField(blank=True, null=True)),
                ("year", models.IntegerField(blank=True, null=True)),
                ("gdp", models.FloatField(blank=True, null=True)),
                ("company_loan", models.FloatField(blank=True, null=True)),
                ("sold_area", models.FloatField(blank=True, null=True)),
                ("completed_area", models.FloatField(blank=True, null=True)),
                ("consumption_index", models.FloatField(blank=True, null=True)),
                ("house_cost", models.FloatField(blank=True, null=True)),
                ("investment", models.FloatField(blank=True, null=True)),
                ("residents_income", models.FloatField(blank=True, null=True)),
                ("land_cost", models.FloatField(blank=True, null=True)),
                ("population", models.FloatField(blank=True, null=True)),
                ("lpr", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="LprPerMonth",
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
                ("year", models.IntegerField(blank=True, null=True)),
                ("month", models.IntegerField(blank=True, null=True)),
                ("lpr", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "LPR_per_month",
                "managed": False,
            },
        ),
    ]
