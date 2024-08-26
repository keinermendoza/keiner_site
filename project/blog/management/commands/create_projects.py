from .base_seader_command import BaseSeaderCommand
from blog.models import Topic
from core.models import Project


class Command(BaseSeaderCommand):
    help = "Creates Porject objects"
    model_class =  Project
    field_to_print = "customer"
    default_number = 10

    def class_faker(self) -> dict:
        customer = self.faker.text()[:30]
        body = self.faker.text()[:150]

        return {
            'title': title,
            'body': body
        }
    
    def many_to_many(self, instance) -> None:
        topic1 = Topic.objects.order_by('?')[0]
        topic2 = Topic.objects.order_by('?')[0]
        topic3 = Topic.objects.order_by('?')[0]

        instance.topics.add(topic1, topic2, topic3)