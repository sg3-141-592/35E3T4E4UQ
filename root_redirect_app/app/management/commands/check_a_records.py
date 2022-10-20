from lib2to3.pytree import Base
from django.core.management.base import BaseCommand, CommandError
from app.models import Site

class Command(BaseCommand):
    help = 'check the a record mapping for site'

    def handle(self, *args, **options):
        self.stdout.write("ABC {}".format(Site.objects.count()))