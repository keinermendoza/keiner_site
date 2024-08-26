from django.test import TestCase
from .models import (
    Topic,
    Post
)

class BlogPostBasicCreation(TestCase):
    """
    minimum fields required by class
    and the __str__ function in each class
    """
    def test_topic_str(self):
        python = Topic.objects.create(name="python")
        self.assertEquals(python.__str__(), "python")

    def test_post_dosent_require_topic_nor_image(self):
        post = Post.objects.create(
            title="Las Tags de Componentes de django-allauth",
            body="Creacion de Landing Page Institucional con las siguientes secciones y funciones:\n\n- Catalogo de Productos y Servicios\n - Testimonios de Clientes\n- Informacion de Contacto\n"
        )
        self.assertIsInstance(post, Post)
        self.assertEquals(post.__str__(), "Las Tags de Componentes de django-allauth")

class BlogPostProperties(TestCase):
    """
    properties of blog class
    """
    def setUp(self) -> None:
        Post.objects.create(
            title="Las Tags de Componentes de django-allauth",
            body="Creacion de Landing Page Institucional con las siguientes secciones y funciones:\n\n- Catalogo de Productos y Servicios\n - Testimonios de Clientes\n- Informacion de Contacto\n"
        )
   
    def test_post_body_html_property(self):
        """body html property returns an html version of the post body field"""
        post = Post.objects.first()
        self.assertEquals(
            post.body_html,
            "<p>Creacion de Landing Page Institucional con las siguientes secciones y funciones:</p>\n<ul>\n<li>Catalogo de Productos y Servicios</li>\n<li>Testimonios de Clientes</li>\n<li>Informacion de Contacto</li>\n</ul>"
        )

    def test_post_preview_property(self):
        """preview property returns the text of the first paragraph in the post body"""
        post = Post.objects.first()
        self.assertEquals(
            post.preview,
            "Creacion de Landing Page Institucional con las siguientes secciones y funciones:"
        )

    def test_post_publish_and_unpublish_method(self):
        """methods for make public or hide an post"""
        post = Post.objects.first()
        self.assertEquals(post.status, Post.Status.EDITING)

        post.publish()
        self.assertEquals(post.status, Post.Status.PUBLISHED)

        post.unpublish()
        self.assertEquals(post.status, Post.Status.EDITING)

class BlogPostManager(TestCase):
    """
    manager for get only the public posts
    """
    def setUp(self) -> None:
        Post.objects.create(
            title="Las Tags de Componentes de django-allauth",
            body="Creacion de Landing Page Institucional con las siguientes secciones y funciones"
        )
        Post.objects.create(
            title="Las Tags",
            body="Creacion de Landing Page Institucional con las siguientes secciones y funciones",
            status=Post.Status.PUBLISHED
        )
        Post.objects.create(
            title="Python",
            body="Creacion de Landing Page Institucional con las siguientes secciones y funciones",
            status=Post.Status.PUBLISHED
        )

    def test_published_manager_get_only_published_posts(self):
        """there is no difference in the queryset obtain by using published manager and filter"""
        posts_using_published = Post.published.all()
        posts_using_filter = Post.objects.filter(status=Post.Status.PUBLISHED)
        self.assertFalse(posts_using_published.difference(posts_using_filter).exists())
