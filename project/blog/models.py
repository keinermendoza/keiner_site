import markdown
from django.db import models
from django.urls import reverse
from django.utils.text import Truncator
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup
from django_extensions.db.fields import AutoSlugField



class Topic(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name



class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)
    
class Post(models.Model):

    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=200, blank=True)

    slug =  AutoSlugField(populate_from='title')
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    topics = models.ManyToManyField(Topic, related_name="posts", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    is_public = models.BooleanField(default=False)
    
    objects = models.Manager()  
    published = PostManager()

    # def publish(self) -> None:
    #     self.status = Post.Status.PUBLISHED
    #     self.save()
    
    # def unpublish(self) -> None:
    #     self.status = Post.Status.EDITING
    #     self.save()

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.slug])
    

    @property
    def body_html(self) -> str:
        return mark_safe(markdown.markdown(self.body))
    
    # @property
    # def preview(self) -> str:
    #     soup = BeautifulSoup(self.body_html, 'html.parser')
    #     first_paragraph = soup.find('p')
    #     return first_paragraph.text if first_paragraph else ""

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields=["-created"])
        ]
        ordering = ["-created"]



class PostImage(models.Model):
    image = models.ImageField(upload_to="post_images")
    alt = models.CharField(max_length=50, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)
