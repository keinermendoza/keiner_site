from .base_seader_command import BaseSeaderCommand
from parafrasis.models import Source

class Command(BaseSeaderCommand):
    model_class = Source
    field_to_print = "name"
    help = "Create Sources in database"

    def class_faker(self) -> dict:
        name = self.faker.unique.first_name()
        return {"name": name}