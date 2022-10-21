from lib2to3.pytree import Base
from django.core.management.base import BaseCommand, CommandError
from app.models import Site

class Command(BaseCommand):
    help = 'check the a record mapping for site'

    def add_arguments(self, parser) -> None:
        parser.add_argument('site_id', nargs='+', type=int)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        print(options['site_id'])
        self.stdout.write("ABC {}".format(Site.objects.count()))