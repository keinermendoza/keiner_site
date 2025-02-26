from django.db import models
from django.utils.safestring import mark_safe
from wagtail.models import Page, Locale
from wagtail.fields import (
    RichTextField,
    StreamField
)
# from wagtail.images.models import Image as WagtailImage
from wagtail import blocks
from wagtail.admin.panels import FieldPanel

from wagtailmetadata.models import MetadataMixin
from wagtailmetadata.models import MetadataPageMixin

from .blocks import (
    CodeBlock,
    AlertBlock,
    GitHubGistBlock
)

from core.forms import ContactForm

class BlogIndexPage(MetadataPageMixin, Page):
    intro = RichTextField(blank=True)  # Texto introductorio opcional

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        """Personaliza el contexto para incluir solo las entradas del idioma activo."""
        context = super().get_context(request)
        context["form"] = ContactForm()
        context["posts"] = BlogPost.objects.live().filter(locale=Locale.get_active()).order_by("-first_published_at")
        return context
    
    # def get_meta_title(self):
    #     """The title of this object"""
    #     return "My custom object"

    # def get_meta_url(self):
    #     """The URL of this object, including protocol and domain"""
    #     return "http://example.com/my-custom-object/"

    # def get_meta_description(self):
    #     """
    #     A short text description of this object.
    #     This should be plain text, not HTML.
    #     """
    #     return "This thing is really cool, you should totally check it out"

    # def get_meta_image_url(self, request):
    #     """
    #     Return a url for an image to use, see the MetadataPageMixin if using a Wagtail image
    #     """
    #     return 'https://neonjungle.studio/share.png'

    # def get_meta_twitter_card_type(self):
    #     """
    #     What kind of Twitter card to show this as.
    #     Defaults to ``summary_large_photo`` if there is a meta image,
    #     or ``summary`` if there is no image. Optional.
    #     """
    #     return "summary_large_photo"


class BlogPost(MetadataPageMixin, Page):
    date = models.DateField("Fecha de publicación", auto_now=True )
    body = StreamField([
        ("rich_Text", blocks.RichTextBlock()),
        ("quotes", blocks.BlockQuoteBlock()),
        # ("gits", GitHubGistBlock()),
        ("mensaje", AlertBlock()),
        ("code", CodeBlock())
    ])
    # body = RichTextField()
    excerpt = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        # FieldPanel("date"),
        FieldPanel("excerpt"),
        FieldPanel("body"),
    ]

    def get_context(self, request):
        context =  super().get_context(request)
        context["form"] = ContactForm()
        return context

