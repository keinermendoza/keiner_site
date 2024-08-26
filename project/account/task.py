from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist
from  allauth.account.adapter import app_settings
from django.core.mail import send_mail
from celery import shared_task
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
import os

             
@shared_task()
def send_feedback_email_task(email_address, name, message):
    """Sends an email when the feedback form has been submitted."""
    subject = "Gracias por entrar en Contacto"
    context = {
        'username':name,
        'message': message
    }
    html_message = render_to_string('templates/core/mail/contact.html', context)

    message = EmailMessage(subject, html_message, os.getenv("EMAIL_HOST_USER"), [email_address])
    message.content_subtype = 'html' # this is required because there is no plain text email message
    message.send()

@shared_task()
def send_mail_to_owner(email_address, name, message):
    send_mail(
        f"Recibiste un mensaje de {name}",
        f"Responder a: {email_address}\n\n{message}",
        os.getenv("EMAIL_HOST_USER"),
        [os.getenv("EMAIL_OWNER")],
        fail_silently=False,
    )

@shared_task()
def send_mail_async(message):
    message.send()


@shared_task()
def async_render_and_send(template_prefix, email, context, headers=None):
    """
    Renders an email to `email`.  `template_prefix` identifies the
    email that is to be sent, e.g. "account/email/email_confirmation"
    """
    to = [email] if isinstance(email, str) else email

    subject = context.pop("subject")
    from_email = context.pop("from_email")

    if "user" in context:
        user = get_user_model().objects.get(pk=context["user"])
        context.update({"user": user})

    current_site = Site.objects.get(pk=context["current_site"])
    context.update({"current_site": current_site})

    bodies = {}
    html_ext = app_settings.TEMPLATE_EXTENSION
    for ext in [html_ext, "txt"]:
        try:
            template_name = "{0}_message.{1}".format(template_prefix, ext)
            bodies[ext] = render_to_string(
                template_name,
                context,
            ).strip()
        except TemplateDoesNotExist:
            if ext == "txt" and not bodies:
                # We need at least one body
                raise
    if "txt" in bodies:
        msg = EmailMultiAlternatives(
            subject, bodies["txt"], from_email, to, headers=headers
        )
        if html_ext in bodies:
            msg.attach_alternative(bodies[html_ext], "text/html")
    else:
        msg = EmailMessage(
            subject, bodies[html_ext], from_email, to, headers=headers
        )
        msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


    # def render_mail(self, template_prefix, email, context, headers=None):
    #     """
    #     Renders an email to `email`.  `template_prefix` identifies the
    #     email that is to be sent, e.g. "account/email/email_confirmation"
    #     """
    #     to = [email] if isinstance(email, str) else email
    #     subject = render_to_string("{0}_subject.txt".format(template_prefix), context)
    #     # remove superfluous line breaks
    #     subject = " ".join(subject.splitlines()).strip()
    #     subject = self.format_email_subject(subject)

    #     from_email = self.get_from_email()

    #     bodies = {}
    #     html_ext = app_settings.TEMPLATE_EXTENSION
    #     for ext in [html_ext, "txt"]:
    #         try:
    #             template_name = "{0}_message.{1}".format(template_prefix, ext)
    #             bodies[ext] = render_to_string(
    #                 template_name,
    #                 context,
    #                 globals()["context"].request,
    #             ).strip()
    #         except TemplateDoesNotExist:
    #             if ext == "txt" and not bodies:
    #                 # We need at least one body
    #                 raise
    #     if "txt" in bodies:
    #         msg = EmailMultiAlternatives(
    #             subject, bodies["txt"], from_email, to, headers=headers
    #         )
    #         if html_ext in bodies:
    #             msg.attach_alternative(bodies[html_ext], "text/html")
    #     else:
    #         msg = EmailMessage(
    #             subject, bodies[html_ext], from_email, to, headers=headers
    #         )
    #         msg.content_subtype = "html"  # Main content is now text/html
    #     return msg
