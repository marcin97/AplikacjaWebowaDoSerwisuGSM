from django.test import TestCase
from hardware.models import HardwareType, HardwareBrand, HardwareModel


class HardwareTypeModelTest(TestCase):
    def setUp(self):
        HardwareType.objects.create(name='Telefon GSM')
        self.hardware_type = HardwareType.objects.get(name='Telefon GSM')

    def test_type_name(self):
        self.assertEqual(self.hardware_type.name, 'Telefon GSM')

    def test_wrong_type_name(self):
        self.assertNotEqual(self.hardware_type.name, 'Tablet')

    def test_name_label(self):
        field_label = self.hardware_type._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Nazwa')

    def test_name_max_length(self):
        max_length = self.hardware_type._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_string_representation(self):
        self.assertEqual(str(self.hardware_type), self.hardware_type.name)


class HardwareBrandTest(TestCase):
    def setUp(self):
        HardwareBrand.objects.create(name='OnePlus')
        self.hardware_brand = HardwareBrand.objects.get(name='OnePlus')

    def test_brand_name(self):
        self.assertEqual(self.hardware_brand.name, 'OnePlus')

    def test_wrong_brand_name(self):
        self.assertNotEqual(self.hardware_brand.name, 'iPhone')

    def test_name_label(self):
        field_label = self.hardware_brand._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Nazwa')

    def test_name_max_length(self):
        max_length = self.hardware_brand._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_string_representation(self):
        self.assertEqual(str(self.hardware_brand), self.hardware_brand.name)


class HardwareModelTest(TestCase):
    def setUp(self):
        hardware_type = HardwareType.objects.create(name='Telefon GSM')
        hardware_brand = HardwareBrand.objects.create(name='OnePlus')
        HardwareModel.objects.create(model='8T', brand=hardware_brand, type=hardware_type, description='test')
        self.hardware_model = HardwareModel.objects.get(model='8T')

    def test_model_field(self):
        self.assertEqual(self.hardware_model.model, '8T')

    def test_wrong_model_field(self):
        self.assertNotEqual(self.hardware_model.model, '9T')

    def test_model_label(self):
        field_label = self.hardware_model._meta.get_field('model').verbose_name
        self.assertEqual(field_label, 'Model')

    def test_model_max_length(self):
        max_length = self.hardware_model._meta.get_field('model').max_length
        self.assertEqual(max_length, 30)

    def test_string_representation(self):
        self.assertEqual(str(self.hardware_model), self.hardware_model.model)
