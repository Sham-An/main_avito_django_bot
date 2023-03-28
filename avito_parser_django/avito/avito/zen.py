# from django.core.management.base import BaseCommand
#
# class Command(BaseCommand):
#     help = 'The Zen of Python'
#
#     def handle(self, *args, **options):
#         import this

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

print(BASE_DIR)