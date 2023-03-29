from django.db import models

from hardware.models import HardwareModel, HardwareType
from main.models import Client
from django.utils.translation import ugettext_lazy as _

STOCK_STATUS = [
    (0, _('Nie')),
    (1, _('Tak')),
]

PAYMENT_TYPE = [
    (0, _('Gotówka')),
    (1, _('Przelew')),
]


class Part(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("Nazwa"))
    type = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("Rodzaj"))
    signature = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("Oznaczenie"))
    description = models.TextField(max_length=255, blank=False, null=False, verbose_name=_("Opis"))
    stock = models.IntegerField(default=1, choices=STOCK_STATUS, verbose_name=_("Na stanie"))
    hardware_model = models.ForeignKey(HardwareModel, on_delete=models.CASCADE, verbose_name=_("Model"))
    hardware_type = models.ForeignKey(HardwareType, default=None, on_delete=models.CASCADE, verbose_name=_("Rodzaj"))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = _("Części")
        verbose_name = _("Części")


class Invoice(models.Model):
    doc_number = models.CharField(max_length=20, blank=False, null=False, verbose_name=_("Nr dokumentu"))
    cost = models.FloatField(default=0.0, blank=False, null=False, verbose_name=_('Kwota'))
    sold_at = models.DateField(null=False, verbose_name=_("Data sprzedaży"))
    due_at = models.DateField(null=False, verbose_name=_("Termin zapłaty"))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("Nabywca"))
    nip = models.CharField(max_length=10, blank=False, null=False, verbose_name=_("NIP"))
    city = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("Miasto"))
    address = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("Adres"))
    post_code = models.CharField(max_length=6, blank=False, null=False, verbose_name=_("Kod pocztowy"))
    payment_type = models.IntegerField(default=0, choices=PAYMENT_TYPE, verbose_name=_("Forma płatności"))

    def __str__(self):
        return f'Faktura: {self.doc_number}'

    class Meta:
        verbose_name_plural = _("Faktura")
        verbose_name = _("Faktury")
