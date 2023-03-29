from django.test import TestCase

from hardware.models import HardwareType, HardwareBrand, HardwareModel
from main.models import Client, Repair


class ClientModelTest(TestCase):
    def setUp(self):
        Client.objects.create(first_name='Jan', last_name='Kowalski', mail='test@test.pl', phone_number='+48123456789',
                              note='test')
        self.client = Client.objects.get(first_name='Jan')

    def test_client_first_name(self):
        self.assertEqual(self.client.first_name, 'Jan')

    def test_wrong_client_first_name(self):
        self.assertNotEqual(self.client.first_name, 'Adam')

    def test_first_name_label(self):
        field_label = self.client._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'Imię')

    def test_name_max_length(self):
        max_length = self.client._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 30)

    def test_string_representation(self):
        self.assertEqual(str(self.client), f'{self.client.first_name} {self.client.last_name}')


class RepairModelTest(TestCase):
    def setUp(self):
        client = Client.objects.create(first_name='Jan', last_name='Kowalski', mail='test@test.pl',
                                       phone_number='+48123456789',
                                       note='test')
        type = HardwareType.objects.create(name='Telefon GSM')
        brand = HardwareBrand.objects.create(name='OnePlus')
        model = HardwareModel.objects.create(model='8T', brand=brand, type=type, description='test')
        Repair.objects.create(description='test', note='test', cost='12.9', client=client, hardware_model=model,
                              hardware_type=type)
        self.repair = Repair.objects.get(description='test')

    def test_repair_description(self):
        self.assertEqual(self.repair.description, 'test')

    def test_wrong_repair_description(self):
        self.assertNotEqual(self.repair.description, 'testy')

    def test_description_label(self):
        field_label = self.repair._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'Opis')

    def test_name_max_length(self):
        max_length = self.repair._meta.get_field('description').max_length
        self.assertEqual(max_length, 255)
