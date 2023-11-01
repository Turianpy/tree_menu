from django.core.management.base import BaseCommand

from menu.models import Menu, MenuItem


class Command(BaseCommand):
    """
    Populates db with data for demo purposes
    """

    def handle(self, *args, **options):

        root_menu = Menu.objects.create(name='gpus', named_url='gpus')
        root_menu.save()

        menu_structure = {
            'name': 'gpus',
            'slug': 'gpus',
            'named_url': 'gpus',
            'children': [
                {'name': 'amd',
                 'slug': 'amd',
                 'named_url': 'brands',
                 'children': [
                     {'name': 'Radeon RX 5000 Series',
                      'slug': 'RX5000',
                      'named_url': 'series',
                      'children': [
                          {'name': 'Radeon RX 5300',
                           'slug': 'RX5300',
                           'named_url': 'model',
                           'children': []},
                          {'name': 'Radeon RX 5700',
                           'slug': 'RX5700',
                           'named_url': 'model',
                           'children': []}]},
                     {'name': 'Radeon RX 6000 Series',
                      'slug': 'RX6000',
                      'named_url': 'series',
                      'children': [
                          {'name': 'Radeon RX 6400',
                           'slug': 'RX6400',
                           'named_url': 'model',
                           'children': []},
                          {'name': 'Radeon RX 6600',
                           'slug': 'RX6600',
                           'named_url': 'model',
                           'children': []}]},
                     {'name': 'Radeon RX 7000 Series',
                      'slug': 'RX7000',
                      'named_url': 'series',
                      'children': [
                          {'name': 'Radeon RX 7600',
                           'slug': 'RX7600',
                           'named_url': 'model',
                           'children': []},
                          {'name': 'Radeon RX 7900 XT',
                           'slug': 'RX7900XT',
                           'named_url': 'model',
                           'children': []}]}]},
                {'name': 'nvidia',
                 'slug': 'nvidia',
                 'named_url': 'brands',
                 'children': [
                     {'name': 'GeForce 30 series',
                      'slug': 'GeForce30',
                      'named_url': 'series',
                      'children': [
                          {'name': 'GeForce RTX 3060',
                           'slug': 'RTX3060',
                           'named_url': 'model',
                           'children': []},
                          {'name': 'GeForce RTX 3070',
                           'slug': 'RTX3070',
                           'named_url': 'model',
                           'url': '', 'children': []}]},
                     {'name': 'GeForce 40 series',
                      'slug': 'GeForce40',
                      'named_url': 'series',
                      'children': [
                          {'name': 'GeForce RTX 4060',
                           'slug': 'RTX4060',
                           'named_url': 'model',
                           'children': []},
                          {'name': 'GeForce RTX 4080',
                           'slug': 'RTX4080',
                           'named_url': 'model',
                           'children': []}]}]}]}

        def create_menu_item(menu_item, parent=None):
            item = MenuItem.objects.create(
                menu=root_menu,
                name=menu_item['name'],
                slug=menu_item['slug'],
                named_url=menu_item['named_url'],
                parent=parent
            )
            item.save()
            for child in menu_item['children']:
                create_menu_item(child, parent=item)

        create_menu_item(menu_structure)

        print('Successfully populated db with demo data')
