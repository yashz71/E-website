# Generated by Django 4.1.1 on 2022-10-04 18:25

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("wagtailcore", "0077_alter_revision_user"),
        ("buyhouse", "0004_remove_buyhousepage_external_page_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="sellhousepage", name="subtitle",),
        migrations.AddField(
            model_name="sellhousepage",
            name="banner_background_image",
            field=models.ForeignKey(
                blank=True,
                help_text="The banner background image",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="sellhousepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "title",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        help_text="Title to display", required=False
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "cards",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Bold title text for this card max length is 140",
                                                        max_length=140,
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.blocks.TextBlock(
                                                        help_text="optianol text for this card max length 250",
                                                        max_length=250,
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        help_text="thsi image will be cropped",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "link",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "link_text",
                                                                wagtail.blocks.CharBlock(
                                                                    default="more details",
                                                                    max_length=50,
                                                                ),
                                                            ),
                                                            (
                                                                "internal_page",
                                                                wagtail.blocks.PageChooserBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                            (
                                                                "external_link",
                                                                wagtail.blocks.URLBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                        ]
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "image_and_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="this image will be cropped"
                                    ),
                                ),
                                (
                                    "image_alignement",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Left"),
                                            ("right", "Right"),
                                            ("center", "Center"),
                                        ],
                                        help_text="image on left and text on right o image on the right and text on the left",
                                    ),
                                ),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="max charachters is 50", max_length=50
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        max_length=140, required=False
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "link_text",
                                                wagtail.blocks.CharBlock(
                                                    default="more details",
                                                    max_length=50,
                                                ),
                                            ),
                                            (
                                                "internal_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.blocks.URLBlock(required=False),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "CTA",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="the max length is 200 charachters",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "link_text",
                                                wagtail.blocks.CharBlock(
                                                    default="more details",
                                                    max_length=50,
                                                ),
                                            ),
                                            (
                                                "internal_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.blocks.URLBlock(required=False),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("pricing_table", streams.blocks.PricingTableBlock()),
                ],
                blank=True,
                null=True,
                use_json_field=None,
            ),
        ),
        migrations.AddField(
            model_name="sellhousepage",
            name="button",
            field=models.ForeignKey(
                blank=True,
                help_text="Select an optional page to link to",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
        migrations.AddField(
            model_name="sellhousepage",
            name="button_text",
            field=models.CharField(
                default="Read More", help_text="Button Text", max_length=50
            ),
        ),
        migrations.AddField(
            model_name="sellhousepage",
            name="description",
            field=models.TextField(blank=True, max_length=440),
        ),
        migrations.CreateModel(
            name="RentHousePage",
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
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "title",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "text",
                                            wagtail.blocks.CharBlock(
                                                help_text="Title to display",
                                                required=False,
                                            ),
                                        )
                                    ]
                                ),
                            ),
                            (
                                "cards",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "cards",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(
                                                                help_text="Bold title text for this card max length is 140",
                                                                max_length=140,
                                                            ),
                                                        ),
                                                        (
                                                            "text",
                                                            wagtail.blocks.TextBlock(
                                                                help_text="optianol text for this card max length 250",
                                                                max_length=250,
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                help_text="thsi image will be cropped",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "link",
                                                            wagtail.blocks.StructBlock(
                                                                [
                                                                    (
                                                                        "link_text",
                                                                        wagtail.blocks.CharBlock(
                                                                            default="more details",
                                                                            max_length=50,
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "internal_page",
                                                                        wagtail.blocks.PageChooserBlock(
                                                                            required=False
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "external_link",
                                                                        wagtail.blocks.URLBlock(
                                                                            required=False
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                    ]
                                                )
                                            ),
                                        )
                                    ]
                                ),
                            ),
                            (
                                "image_and_text",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                help_text="this image will be cropped"
                                            ),
                                        ),
                                        (
                                            "image_alignement",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    ("left", "Left"),
                                                    ("right", "Right"),
                                                    ("center", "Center"),
                                                ],
                                                help_text="image on left and text on right o image on the right and text on the left",
                                            ),
                                        ),
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(
                                                help_text="max charachters is 50",
                                                max_length=50,
                                            ),
                                        ),
                                        (
                                            "text",
                                            wagtail.blocks.CharBlock(
                                                max_length=140, required=False
                                            ),
                                        ),
                                        (
                                            "link",
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "link_text",
                                                        wagtail.blocks.CharBlock(
                                                            default="more details",
                                                            max_length=50,
                                                        ),
                                                    ),
                                                    (
                                                        "internal_page",
                                                        wagtail.blocks.PageChooserBlock(
                                                            required=False
                                                        ),
                                                    ),
                                                    (
                                                        "external_link",
                                                        wagtail.blocks.URLBlock(
                                                            required=False
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "CTA",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(
                                                help_text="the max length is 200 charachters",
                                                max_length=200,
                                            ),
                                        ),
                                        (
                                            "link",
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "link_text",
                                                        wagtail.blocks.CharBlock(
                                                            default="more details",
                                                            max_length=50,
                                                        ),
                                                    ),
                                                    (
                                                        "internal_page",
                                                        wagtail.blocks.PageChooserBlock(
                                                            required=False
                                                        ),
                                                    ),
                                                    (
                                                        "external_link",
                                                        wagtail.blocks.URLBlock(
                                                            required=False
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            ("pricing_table", streams.blocks.PricingTableBlock()),
                        ],
                        blank=True,
                        null=True,
                        use_json_field=None,
                    ),
                ),
                (
                    "button_text",
                    models.CharField(
                        default="Read More", help_text="Button Text", max_length=50
                    ),
                ),
                (
                    "banner_background_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="The banner background image",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "button",
                    models.ForeignKey(
                        blank=True,
                        help_text="Select an optional page to link to",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("wagtailcore.page",),
        ),
    ]