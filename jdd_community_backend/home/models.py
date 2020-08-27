from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    # Call to action
    cta_headline = models.CharField(max_length=50)
    cta_sub_headline = RichTextField(blank=True, null=True)
    cta_button_text = models.CharField(max_length=20)
    cta_button_url = models.URLField(blank=True, null=True)
    

    content_panels = Page.content_panels + [
        FieldPanel('cta_headline', classname="full"),
        FieldPanel('cta_sub_headline', classname="full"),
        FieldPanel('cta_button_text', classname="full"),
        FieldPanel('cta_button_url', classname="full"),
    ]


