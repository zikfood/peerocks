from common.management.commands.products import (
    create_products,
)
from common.management.commands.recipes import (
    create_recipes,
)
from common.management.commands.users import (
    create_users,
)
from django.core.management.base import (
    BaseCommand,
)


class Command(BaseCommand):
    args = '<>'
    help = 'Prepares the database'

    def handle(self, *args, **options):

        self.stdout.write('Preparing db data\n')

        create_users()
        create_products()
        create_recipes()

        self.stdout.write('Successfully complete\n')
