from django.db import models
from wagtail.core.models import Page

class LoginPage(Page):
     description = models.TextField(
        blank=True,
        max_length=440,
    )
