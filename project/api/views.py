from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView  
from .forms import ContactEmail
from account.utils import SendMailTo 
from core.models import (
    Testimonial,
    Project
)
from .serializers import (
    TestimonialSerializer,
    ProjectSerializer
)

class TestimonialListCreateAPIView(ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class ProjectsListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



# def email_contact(request):
#     if request.method == 'POST':
#         form = ContactEmail(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             print(cd)
#             try:
#                 SendMailTo.anonimo_contact(cd['name'], cd['email'], cd['message'])
#             except:
#                 return JsonResponse({'error':'Sorry, email service is not available at the moment.'}, status=400)

#             # send email to me with the content and sender
#             # send authomatic message to the user
#             return JsonResponse({'message':'Email Suceffully Sended, Check out your email inbox'}, status=200)
#         else:
#             return JsonResponse({'error':"Please check if there is a misstype in the email field. It's not a valid email."}, status=400)
        
#     return JsonResponse(status=405)
