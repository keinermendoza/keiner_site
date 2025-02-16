from django import template
from django.utils.translation import gettext_lazy as _

register = template.Library()

@register.simple_tag
def get_navlinks():
    """returns the main links for navigation in public site"""
    links =[{'text': _("Home"), 'href':'/'}, {'text':_("Blog"), 'href':'/blog' }]
    return links