from django.core.mail import EmailMessage
import os
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
# from rest_framework_simplejwt.tokens import RefreshToken




class SendMailTo:
    """Class for handle the send of email based on html
    to users authenticated or to a valid email direction"""

    SITE = 'https://keinermendoza.com/'
    FROM_EMAIL = 'From keiner@example.com'
    WEBSITE_NAME = "Keiner's blog"

    def __init__(self, user_instance):
        self.user = user_instance
        self.subject = None
        self.html_message = None
        self.plain_message = None

    @classmethod
    def anonimo_contact(cls, username, email, message):
        """sends a contact message to an email direction
            dosen't require a user instance"""
        
        subject = "Gracias por entrar en Contacto"
        context = {
            'username':username,
            'message': message
        }
        html_message = render_to_string('account/mail/contact.html', context)

        ### this options attach a file to an email, it could be usefully for other case
        # message = EmailMultiAlternatives(
        #     subject,
        #     body_html,
        #     from_email=cls.FROM_EMAIL,
        #     to=[email]
        # )

        # message.mixed_subtype = 'related'
        # message.attach_alternative(body_html, "text/html")
        # img_dir = 'static'
        # image = 'profile.jpg'
        # # file_path = os.path.join(img_dir, image)
        # file_path = 'blog/static/blog/images/profile.jpg'

        # with open(file_path, 'rb') as f:
        #     img = MIMEImage(f.read())
        #     img.add_header('Content-ID', '<{name}>'.format(name=image))
        #     img.add_header('Content-Disposition', 'inline', filename=image)
        # message.attach(img)

        message = EmailMessage(subject, html_message, cls.FROM_EMAIL, [email])
        message.content_subtype = 'html' # this is required because there is no plain text email message
        message.send()


    def wellcome_email(self):
        """sends a wellcome message to the current user
            REQUIRE A USER INSTANCE"""
        
        context = {
            'username': self.user.username,
            'website': self.WEBSITE_NAME,
            'date' : timezone.now(),
            'url': self.SITE,
        }

        self.subject = "Wellcome to the Keiner's Blog"
        self.html_message = render_to_string('account/mail/wellcome.html', context)
        self.plain_message = strip_tags(self.html_message)
        self.send()

    # def authentication_email(self):
    #     """sends an email with the url-token authentication for new users
    #     REQUIRE A USER INSTANCE"""

    #     token = RefreshToken.for_user(self.user)

    #     context = {
    #         'username': self.user.username,
    #         'website': self.WEBSITE_NAME,
    #         'date' : timezone.now(),
    #         'url': self.SITE + str(token),
    #     }

    #     self.subject = "Validate your email on Keiner's Blog"
    #     self.html_message = render_to_string('account/mail/authenticate.html', context)
    #     self.plain_message = strip_tags(self.html_message)
    #     self.send()

    def send(self):
        """sends an email using the current values of the Mail class and instance
        REQUIRE A USER INSTANCE"""

        message = EmailMessage(self.subject, self.html_message, self.FROM_EMAIL, [self.user.email])
        message.content_subtype = 'html' # this is required because there is no plain text email message
        message.send()
