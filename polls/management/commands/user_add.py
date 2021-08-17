from django.core.management.base import BaseCommand, CommandError

from faker import Faker

from polls.models import PollsUser as Pu


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 11),  help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        number = kwargs['total']
        try:
            fake = Faker()
            list_pu = []
            for i in range(number):
                list_pu.append(Pu(username=fake.name(), email=fake.ascii_email(),
                                  password=fake.swift()))
            Pu.objects.bulk_create(list_pu)
            self.stdout.write('Successfully created')
        except Pu.DoesNotExist:
            raise CommandError("The number must be in the range 1 to 10")
