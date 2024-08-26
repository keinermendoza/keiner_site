from typing import Any
from faker import Faker
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandParser


class BaseSeaderCommand(BaseCommand):
    """
    Abstract class for seed a table using djnago model.Model class
    model_class: the class you want to use for populate
    field_to_print: [optional] field of model you want to print in console
    default_number: number of instances to be created if the param '-n' '--number' it is not provided
    """

    faker = Faker()
    default_number = 10
    model_class = None
    field_to_print = None

    def class_faker(self) -> dict:
        """
        You can use the faker, must to return a dict with the names and values of the model_class
        if your model is:

            Country(models.Model):
                name = models.Charfield(max_length=100)

        this method can return:
            return {'name': 'Mexico'}
        """
        raise NotImplementedError(
            "You must to provide your own implementation of the method class_faker see managment/commands/base_seader_commands.py"
        )
    
    def many_to_many(self, instance) -> None:
        pass

    def create(self, create_number: int) -> None:
        """
        create the specified 'number' (or default_number) of instances
        and print to console if field_to_print is defined
        """
        if create_number <= 0:
            exit(f"'-n' argument cannot be equal or less than 0")

        created = 0
        while created < create_number:

            params = self.class_faker()
            try:
                created_object = self.model_class.objects.create(**params)

            except IntegrityError:
                continue

            except Exception as e:
                exit(f"aborting due to {e}")

            else:
                created += 1
                if self.field_to_print and hasattr(created_object, self.field_to_print):

                    object_name = getattr(created_object, self.field_to_print)
                    if callable(object_name):
                        object_name = object_name()
                    self.stdout.write(f"Created {object_name}")
                
                self.many_to_many(created_object)

                

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            help=f"set the number of {self.model_class._meta.model_name} to be created",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        """main function"""

        number_create = options.get("number", None)
        if number_create is None:
            number_create = self.default_number

        self.create(number_create)

        self.stdout.write(
            self.style.SUCCESS(
                f"{number_create} {self.model_class._meta.model_name} succeffully created"
            )
        )
