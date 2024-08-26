from .base_seader_command import BaseSeaderCommand
from django.contrib.auth import get_user_model
from parafrasis.models import ExpressionComment, Expression

User = get_user_model()

class Command(BaseSeaderCommand):
    help = "Creates ExpressionComment objects"
    model_class =  ExpressionComment
    field_to_print = "__str__"
    default_number = 10

    def class_faker(self) -> dict:
        user = User.objects.order_by('?')[0]
        expression = Expression.objects.order_by('?')[0]
        body = self.faker.text()[:150]

        return {
            'user': user,
            'expression': expression,
            'body': body
        }