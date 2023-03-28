# from django.core.management.base import BaseCommand
#
# class Command(BaseCommand):
#     help = 'The Zen of Python'
#
#     def handle(self, *args, **options):
#         import this

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR1 = Path(__file__).resolve().parent.parent
BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR1)
print(BASE_DIR2)
