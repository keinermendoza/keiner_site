from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Post, Topic

class Command(BaseCommand):
    """
    populate the topics and posts tables with fake data
    """

    def register_topics(self):
        try:
            self.python = Topic.objects.create(name="python")
            self.django = Topic.objects.create(name="django")
            self.rest = Topic.objects.create(name="django resst framework")
            self.javascript = Topic.objects.create(name="javascript")
            self.html = Topic.objects.create(name="html")
            self.css = Topic.objects.create(name="css")
            self.tailwindcss = Topic.objects.create(name="tailwindcss")
            self.postgresql = Topic.objects.create(name="postgresql")
            self.mysql = Topic.objects.create(name="mysql")

        except IntegrityError as e:
            self.stdout.write(
                self.style.ERROR("topics dosent registered suceffully")
            )
            raise e

    def register_posts(self):
        try:
            components = Post.objects.create(
                title = "Las Tags de Componentes de django-allauth",
                body = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste minus id, architecto ipsum numquam eius!",
            )
            components.topics.add(self.django, self.javascript)

            celery_allauth = Post.objects.create(
                title = "Celery con django-allatuh sin dependencias extras",
                body = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste minus id, architecto ipsum numquam eius!",
            )
            celery_allauth.topics.add(self.django, self.html)

            celery = Post.objects.create(
                title = "Las Tags de Componentes de django",
                body = "string"
            )
            celery.topics.add(self.django, self.rest)

        except IntegrityError as e:
            self.stdout.write(
                self.style.ERROR("posts dosent registered suceffully")
                
            )
            raise e
        
    def handle(self, *args, **options) -> str | None:
        """main function"""
        try:
            self.register_topics()
            self.register_posts()

        except IntegrityError:
            self.stdout.write(
                self.style.ERROR,
                "data not registered"
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("base data succeffully registered")
            )
