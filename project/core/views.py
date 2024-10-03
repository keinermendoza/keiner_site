from typing import Any, List
from django.db.models import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    TemplateView,
    FormView
    
)
from .mock import projects

from django_htmx.http import trigger_client_event

from .permissions import IsAdmin
from .forms import (
    ContactForm
)

from core.models import (
    Testimonial,
    Project
)

from blog.models import (
    Post
)
def simple_home(request):
    form = ContactForm()
    return render(request, "pages/home/new_desing.html", {"form":form})

class HomePage(TemplateView):
    template_name = "core/pages/home.html"
    PROJECT_LIMIT :int = 2
    POST_LIMIT :int = 3
    TESTIMONIALS_LIMIT :int = 3


    def get_testimonials(self) -> QuerySet[Testimonial]:
        return Testimonial.published.all()[:self.TESTIMONIALS_LIMIT]

    def get_projects(self) -> list:
        # return projects
        return Project.published.all()[:self.PROJECT_LIMIT]
    
    def get_posts(self) -> QuerySet[Post]:
        """last published posts"""
        return Post.published.all()[:self.POST_LIMIT]
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            "projects": self.get_projects(),
            "testimonials": self.get_testimonials(),
            "posts": self.get_posts()
        })
        return context
    
class AboutPage(TemplateView):
    template_name = "core/pages/about.html"
    PROJECT_LIMIT :int = 2
    POST_LIMIT :int = 3

class ContactFormPartialView(FormView):
    form_class = ContactForm
    # template_name = "cotton/layouts/contact_form.html"
    template_name = "cotton/forms/contact_form.html"

    def form_valid(self, form) -> HttpResponse:
        response = self.render_to_response({'form':form})
        return trigger_client_event(
            response,
            "display_toast",
            {
                "status":200,
                "message":"Email Enviado. Revisa la Bandeja de Entrada de tu Correo"
            }
        )
    
    def form_invalid(self, form) -> HttpResponse:
        response = super().form_invalid(form)
        return trigger_client_event(
            response,
            "display_toast",
            {
                "status":400,
                "message":"No fue posible enviar el mensaje"
            }
        )   

    def post(self, request, *args, **kwargs):
        """
        Sends Async Email
        """
        form = self.get_form()
        if form.is_valid():
            # form.send_email()
            return self.form_valid(form)
        else:
            if "username" in form.errors:
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

class EditorView(IsAdmin, TemplateView):
    template_name = "core/pages/editor.html"
