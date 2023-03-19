from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.models import Page
from streams import blocks



class HomePage(Page):
    lead_text = models.CharField(
        max_length=140,
        blank=True,
        help_text='Subheading text under the banner title',
    )
    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardBlock()),
        ("image_and_text", blocks.ImagesAndTextBlock()),
        ("CTA", blocks.CallToAction()),
        ("pricing_table", blocks.PricingTableBlock()),
    ], null=True, blank=True,)
    button = models.ForeignKey(
        'wagtailcore.page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optional page to link to',
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=50,
        default='Read More',
        blank=False,
        help_text='Button Text'
    )
    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name='+',
        help_text='The banner background image',
        on_delete=models.SET_NULL,
    )
    content_panels = Page.content_panels + [
         StreamFieldPanel("body"),

    ]
