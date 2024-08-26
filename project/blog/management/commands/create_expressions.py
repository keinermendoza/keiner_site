from .base_seader_command import BaseSeaderCommand
from django.contrib.auth import get_user_model
from parafrasis.models import Expression

User = get_user_model()

class Command(BaseSeaderCommand):
    help = "Creates Expression objects"
    model_class =  Expression
    field_to_print = "expression"
    default_number = 10

    def class_faker(self) -> dict:
        author = User.objects.order_by('?')[0]
        expression = self.faker.text()[:30]
        parafrasis = self.faker.text()[:150]

        return {
            'author': author,
            'expression': expression,
            'parafrasis': parafrasis
        }