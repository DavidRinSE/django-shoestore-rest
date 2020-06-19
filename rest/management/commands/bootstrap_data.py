from django.core.management.base import BaseCommand, CommandError
from rest.models import ShoeType, ShoeColor

SHOE_COLOR_CHOICES = [
    ('(255,0,0)', 'Red'),
    ('(255,165,0)', 'Orange'),
    ('(255,255,0)', 'Yellow'),
    ('(0,255,0)', 'Green'),
    ('(0,0,255)', 'Blue'),
    ('(29,0,51)', 'Indigo'),
    ('(238,130,230)', 'Violet'),
    ('(255,255,255)', 'White'),
    ('(0,0,0)', 'Black'),
]

SHOE_TYPES = [
    'Sneaker',
    'Boot',
    'Sandal',
    'Dress',
    'Other'
]

class Command(BaseCommand):
    help = "Seeds database with shoe color and type"

    def handle(self, *args, **options):
        for choice in SHOE_COLOR_CHOICES:
            ShoeColor.objects.create(color_name=choice[0])
        for shoe_type in SHOE_TYPES:
            ShoeType.objects.create(style=shoe_type)
