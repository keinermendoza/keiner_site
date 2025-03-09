from typing import Any
from re import findall
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .task import (
    send_feedback_email,
    send_mail_to_owner
)



class ContactForm(forms.Form):
    # https://docs.djangoproject.com/en/5.0/topics/forms/?source=post_page-----5f867f25f153--------------------------------#reusable-form-templates
    template_name = "core/forms/base_form.html"

    name = forms.CharField(
        label=_("Name"),
        max_length=100
    )
    best_email = forms.EmailField(
        label=_("Email")
    )
    message = forms.CharField(
        label=_("Message"),
        widget=forms.Textarea(attrs={'rows':3})
    )
   
    
    # trap fields
    username = forms.CharField(
        required=False,
        widget=forms.HiddenInput()    
    )
    email = forms.CharField(
        required=False,
        widget=forms.HiddenInput()    
    )

    def clean_message(self):
        if message := self.cleaned_data.get("message", None):
            
            if len(findall(r"://", message)):
                self.add_error("message", _("Sorry, you cannot include links in the message"))
            return message
    
    def clean(self) -> dict[str, Any]:
        """
        checking fields for catch some bots
        """
        cleaned_data = super().clean()
        trap1 = cleaned_data.get("email")
        trap2 = cleaned_data.get("username")

        if trap1 or trap2:
            self.add_error("username", "stop the bot")
        return cleaned_data
    
    def send_email(self, lang) -> None:
        """
        using celery task for send emails
        """
        email = self.cleaned_data.get("best_email")
        name = self.cleaned_data.get("name")
        message = self.cleaned_data.get("message")
        send_feedback_email.delay(email, name, message, lang)
        send_mail_to_owner.delay(email, name, message)

