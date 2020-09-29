"""
@@TODO
"""

from textwrap import dedent
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = dedent(__doc__).strip()

    def add_arguments(self, parser):
        _ = parser
        pass

    def handle(self, *args, **options):
        pass
