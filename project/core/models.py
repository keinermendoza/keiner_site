
import markdown
from django.db import models
# from blog.models import Topic
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from .validators import for_published_status_require_image_not_none

class TestimonialManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)

class Testimonial(models.Model):

    name = models.CharField(max_length=40)
    profession = models.CharField(max_length=80)
    message = models.CharField(max_length=250)
    image = models.ImageField(upload_to="testimonials", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # status = models.CharField(max_length=1, choices=Status.choices, default=Status.EDITING)
    is_public = models.BooleanField(default=False)

    objects = models.Manager()  
    published = TestimonialManager()

    # def clean(self):
    #     for_published_status_require_image_not_none(self.status, self.image)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    # def publish(self) -> None:
    #     self.status = Project.Status.PUBLISHED
    #     self.save()
    
    # def unpublish(self) -> None:
    #     self.status = Project.Status.EDITING
    #     self.save()

    def __str__(self) -> str:
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["-created"])
        ]
        ordering = ["-created"]

class ProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)
    
class Project(models.Model):
    class Status(models.TextChoices):
        EDITING = ("E", "Editing")
        PUBLISHED = ("P", "Published")

    customer = models.CharField(max_length=40)
    customer_commercial_field = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # tecnologies = models.ManyToManyField(Topic, related_name="projects", blank=True)
    is_public = models.BooleanField(default=False)
    video_demo = models.URLField(null=True, blank=True)
    
    objects = models.Manager()  
    published = ProjectManager()


    # def clean(self):
    #     for_published_status_require_image_not_none(self.status, self.image)

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)
    
    @property
    def description_html(self) -> str:
        return mark_safe(markdown.markdown(self.description))
    
    @property
    def get_images_mobile(self) -> models.QuerySet:
        return self.images.filter(device="M")
    
    @property
    def get_images_desktop(self) -> models.QuerySet:
        return self.images.filter(device="D")
    
    # def publish(self) -> None:
    #     self.status = Project.Status.PUBLISHED
    #     self.save()
    
    # def unpublish(self) -> None:
    #     self.status = Project.Status.EDITING
    #     self.save()

    def __str__(self) -> str:
        return self.customer

    class Meta:
        indexes = [
            models.Index(fields=["-created"])
        ]
        ordering = ["-created"]


class ProjectImage(models.Model):
    class Device(models.TextChoices):
        MOBILE = ("M", "Mobile")
        DESKTOP = ("D", "Desktop")
    image = models.ImageField(upload_to="project_images")
    alt = models.CharField(max_length=50, null=True, blank=True)
    device = models.CharField(max_length=1, choices=Device.choices, default=Device.DESKTOP)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")