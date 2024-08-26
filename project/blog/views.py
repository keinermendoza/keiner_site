# EDIT
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django_htmx.http import HttpResponseClientRefresh
from django_htmx.http import retarget
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin

from django.http import QueryDict

from django.views.generic import (
    ListView,
    DeleteView,
    View
)
from .filters import PostFilter
from .models import (
    Post
)


class BlogPageList(ListView):
    model = Post
    paginate_by = 9
    context_object_name = "posts"
    template_name = "blog/pages/list.html"

    # custom attributes
    filter_class = PostFilter
    template_partial = "cotton/layouts/blog/paginated_list.html"

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return [self.template_partial]
        return super().get_template_names()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        page = context['page_obj']
        context.update({
            "filter": self.filter_class(),
            "elided_page_range": page.paginator.get_elided_page_range(page.number, on_each_side=2, on_ends=1)
        })
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return self.filter_queryset(queryset)
    
    def filter_queryset(self, queryset) -> QuerySet[Any]:
        filter = self.filter_class(self.request.GET, queryset)
        return filter.qs

class BlogPageDetail(DeleteView):
    model = Post
    context_object_name = "post"
    template_name = "blog/pages/detail.html"

