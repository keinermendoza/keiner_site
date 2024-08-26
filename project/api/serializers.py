from rest_framework import serializers
from core.models import (
    Testimonial,
    Project
)

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        exclude = ['created', 'updated']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['created', 'updated']
