# Generated by Django 4.1 on 2023-11-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analyzer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
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
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
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
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
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
                ("codename", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
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
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.BooleanField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.BooleanField()),
                ("is_active", models.BooleanField()),
                ("date_joined", models.DateTimeField()),
                ("first_name", models.CharField(max_length=150)),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
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
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
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
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="BackgroundTask",
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
                ("task_name", models.CharField(max_length=190)),
                ("task_params", models.TextField()),
                ("task_hash", models.CharField(max_length=40)),
                (
                    "verbose_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("priority", models.IntegerField()),
                ("run_at", models.DateTimeField()),
                ("repeat", models.BigIntegerField()),
                ("repeat_until", models.DateTimeField(blank=True, null=True)),
                ("queue", models.CharField(blank=True, max_length=190, null=True)),
                ("attempts", models.IntegerField()),
                ("failed_at", models.DateTimeField(blank=True, null=True)),
                ("last_error", models.TextField()),
                ("locked_by", models.CharField(blank=True, max_length=64, null=True)),
                ("locked_at", models.DateTimeField(blank=True, null=True)),
                (
                    "creator_object_id",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
            ],
            options={
                "db_table": "background_task",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="BackgroundTaskCompletedtask",
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
                ("task_name", models.CharField(max_length=190)),
                ("task_params", models.TextField()),
                ("task_hash", models.CharField(max_length=40)),
                (
                    "verbose_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("priority", models.IntegerField()),
                ("run_at", models.DateTimeField()),
                ("repeat", models.BigIntegerField()),
                ("repeat_until", models.DateTimeField(blank=True, null=True)),
                ("queue", models.CharField(blank=True, max_length=190, null=True)),
                ("attempts", models.IntegerField()),
                ("failed_at", models.DateTimeField(blank=True, null=True)),
                ("last_error", models.TextField()),
                ("locked_by", models.CharField(blank=True, max_length=64, null=True)),
                ("locked_at", models.DateTimeField(blank=True, null=True)),
                (
                    "creator_object_id",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
            ],
            options={
                "db_table": "background_task_completedtask",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
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
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
                ("action_time", models.DateTimeField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
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
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
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
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
    ]
