from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
import re
from urllib.parse import quote

register = template.Library()
# https://api.whatsapp.com/send?phone=556592823891
@register.filter(name="whatsapp_link")
def scape_text(text):
    whatsapp_base = 'https://api.whatsapp.com/send?phone=' + settings.WHATSAPP_NUMBER
    if text:
        cleaned_text = re.sub(r'\s+', ' ', text)
        quoted_text = quote(cleaned_text)
        whatsapp_base = whatsapp_base + '&text=' + quoted_text
    return mark_safe(whatsapp_base)