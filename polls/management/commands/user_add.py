from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password

from faker import Faker

from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 11),  help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        User = get_user_model()
        number = kwargs['total']
        try:
            fake = Faker()
            list_pu = []
            for i in range(number):
                list_pu.append(User(username=fake.name(), email=fake.ascii_email(),
                                  password=make_password(fake.swift())))
            User.objects.bulk_create(list_pu)
            self.stdout.write('Successfully created')
        except User.DoesNotExist:
            raise CommandError("The number must be in the range 1 to 10")
