from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPageList.as_view(), name='list'),
    path('<slug:slug>', views.BlogPageDetail.as_view(), name='detail'),

]
