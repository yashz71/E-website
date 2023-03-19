# Generated by Django 4.1.1 on 2022-10-04 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0077_alter_revision_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUsPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("description", models.TextField(blank=True, max_length=440)),
            ],
            options={"abstract": False,},
            bases=("wagtailcore.page",),
        ),
    ]
