import re
from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def remove_page_param(url):
    """
    Removes page param from the url using regex
    """
    pattern = r"[?&]{1}page\=\d+"
    cleaned_url = re.sub(pattern, "", url)
    if "?" in cleaned_url:
        return cleaned_url + "&"
    return cleaned_url + "?"

@register.filter
def clean_amperson(url):
    """
    call static and mark url as safe
    """
    amp_url = static(url)
    cleaned_url = mark_safe(amp_url)
    return cleaned_url
