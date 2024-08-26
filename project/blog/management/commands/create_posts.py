from .base_seader_command import BaseSeaderCommand
from blog.models import Post, Topic


class Command(BaseSeaderCommand):
    help = "Creates Post objects"
    model_class =  Post
    field_to_print = "post"
    default_number = 10

    def class_faker(self) -> dict:
        title = self.faker.text()[:30]
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