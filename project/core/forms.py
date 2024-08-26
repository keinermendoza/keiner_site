from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from .task import (
    send_feedback_email,
    send_mail_to_owner
)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    best_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    # trap fields
    username = forms.CharField(required=False)
    email = forms.CharField(required=False)
    
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
    
    def send_email(self) -> None:
        """
        using celery task for send emails
        """
        email = self.cleaned_data.get("best_email")
        name = self.cleaned_data.get("name")
        message = self.cleaned_data.get("message")
        send_feedback_email.delay(email, name, message)
        send_mail_to_owner.delay(email, name, message)

