from django.core.management.base import BaseCommand
import os

from config.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        firstname = os.environ.get('DJANGO_SUPERUSER_FIRST_NAME')
        lastname = os.environ.get('DJANGO_SUPERUSER_LAST_NAME')
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not CustomUser.objects.filter(username=username).exists():
            print('Creating account for %s (%s)' % (username, email))
            admin = CustomUser.objects.create_superuser(
                first_name=firstname, last_name=lastname,
                email=email, username=username, password=password)
        else:
            print('Admin account has already been initialized.')
