from django.db import models
from wagtail.core.models import Page

class RentChoicePage(Page):
     description = models.TextField(
        blank=True,
        max_length=440,
    )
