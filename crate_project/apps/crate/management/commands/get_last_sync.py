import redis

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        r = redis.StrictRedis(**getattr(settings, "PYPI_DATASTORE_CONFIG", {}))
        print r.get("crate:pypi:since")
