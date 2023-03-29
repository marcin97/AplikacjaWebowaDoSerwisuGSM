import datetime

from django.test import TestCase

from hardware.models import HardwareType, HardwareBrand, HardwareModel
from main.models import Client
from utility.models import Part, Invoice


class PartModelTest(TestCase):
    def setUp(self):
        hardware_type = HardwareType.objects.create(name='Telefon GSM')
        hardware_brand = HardwareBrand.objects.create(name='OnePlus')
        hardware_model = HardwareModel.objects.create(model='8T', brand=hardware_brand, type=hardware_type,
                                                      description='test')
        Part.objects.create(name='Szklo ochronne', type='akcesoria', signature='XB21CZ37', description='test',
                            hardware_type=hardware_type, hardware_model=hardware_model)
        self.part = Part.objects.get(name='Szklo ochronne')

    def test_part_name(self):
        self.assertEqual(self.part.name, 'Szklo ochronne')

    def test_wrong_part_name(self):
        self.assertNotEqual(self.part.name, 'Klapa')

    def test_first_name_label(self):
        field_label = self.part._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Nazwa')

    def test_name_max_length(self):
        max_length = self.part._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_string_representation(self):
        self.assertEqual(str(self.part), self.part.name)


class InvoiceModelTest(TestCase):
    def setUp(self):
        client = Client.objects.create(first_name='Jan', last_name='Kowalski', mail='test@test.pl',
                                       phone_number='+48123456789',
                                       note='test')
        Invoice.objects.create(doc_number='2137', cost=12.0, sold_at=datetime.date.today(),
                               due_at=datetime.date.today(), client=client, nip='2137', city='Bialystok', address='Test',
                               post_code='15-111')
        self.invoice = Invoice.objects.get(doc_number='2137')

    def test_invoice_first_name(self):
        self.assertEqual(self.invoice.doc_number, '2137')

    def test_wrong_invoice_first_name(self):
        self.assertNotEqual(self.invoice.doc_number, '2173')

    def test_first_name_label(self):
        field_label = self.invoice._meta.get_field('doc_number').verbose_name
        self.assertEqual(field_label, 'Nr dokumentu')

    def test_name_max_length(self):
        max_length = self.invoice._meta.get_field('doc_number').max_length
        self.assertEqual(max_length, 20)

    def test_string_representation(self):
        self.assertEqual(str(self.invoice), f'Faktura: {self.invoice.doc_number}')
