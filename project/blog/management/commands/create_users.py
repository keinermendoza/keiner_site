from .base_seader_command import BaseSeaderCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class Command(BaseSeaderCommand):
    help = "Creates Users objects, based on the registered user model"
    model_class = get_user_model()
    field_to_print = "username"
    default_number = 3

    def class_faker(self) -> dict:
        username = self.faker.unique.first_name()
        email = f"{username}@gmail.com"
        password = make_password(self.faker.first_name())
        
        return {
            'username': username,
            'email': email,
            'password': password
        }