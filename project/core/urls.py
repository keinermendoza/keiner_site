from django.urls import path, re_path
from . import views
from . import assets_view
from django.views.generic import RedirectView, TemplateView
app_name = 'core'

urlpatterns = [
    # path("", views.HomePage.as_view(), name="home"),
    path("", views.simple_home, name="home"),
    path("signed-css", assets_view.css_view, name="css_view"),
    # path("", TemplateView.as_view(template_name="pages/home/new_desing.html"), name="home"),
    path("about", views.AboutPage.as_view(), name="about"),
    path("contact-me", views.ContactFormPartialView.as_view(), name="contact_me"),
    path("editor", views.EditorView.as_view(), name="editor"),
    re_path(r'^editor/.*$', views.EditorView.as_view()),
    # re_path(r'^editor/.*$', RedirectView.as_view(pattern_name="core:editor")),

]
