from django.db import models
from django.utils.safestring import mark_safe
from wagtail.models import Page, Locale
from wagtail.fields import (
    RichTextField,
    StreamField
)
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from .blocks import (
    CodeBlock,
    AlertBlock,
    GitHubGistBlock
)

from core.forms import ContactForm

class BlogIndexPage(Page):
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


class BlogPost(Page):
    date = models.DateField("Fecha de publicación")
    body = StreamField([
        ("rich_Text", blocks.RichTextBlock()),
        ("quotes", blocks.BlockQuoteBlock()),
        ("gits", GitHubGistBlock()),
        ("mensaje", AlertBlock()),
        ("code", CodeBlock())
    ])
    # body = RichTextField()
    excerpt = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("excerpt"),
        FieldPanel("body"),
    ]

    def get_context(self, request):
        context =  super().get_context(request)
        context["form"] = ContactForm()
        return context

