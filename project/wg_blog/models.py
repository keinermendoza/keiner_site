from django.db import models
from wagtail.models import Page, Locale
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)  # Texto introductorio opcional

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        """Personaliza el contexto para incluir solo las entradas del idioma activo."""
        context = super().get_context(request)
        context["posts"] = BlogPost.objects.live().filter(locale=Locale.get_active()).order_by("-first_published_at")
        return context


class BlogPost(Page):
    date = models.DateField("Fecha de publicación")
    body = RichTextField()
    excerpt = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("excerpt"),
        FieldPanel("body"),
    ]