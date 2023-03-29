from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _

from hardware.models import HardwareModel, HardwareType

REPAIR_STATUS = [
    (0, _('Nowy')),
    (1, _('W trakcie')),
    (2, _('Błąd')),
    (3, _('Naprawiony'))
]


class Client(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False, verbose_name=_("Imię"))
    last_name = models.CharField(max_length=30, blank=False, null=False, verbose_name=_("Nazwisko"))
    mail = models.EmailField(max_length=50, blank=False, null=False, verbose_name=_("Email"))
    phone_number = PhoneNumberField(verbose_name=_("Numer telefonu"))
    note = models.TextField(max_length=255, blank=False, null=False, verbose_name=_("Uwagi"))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = _("Klienci")
        verbose_name = _("Klient")


class Repair(models.Model):
    repair_status = models.IntegerField(default=0, choices=REPAIR_STATUS, verbose_name=_("Status naprawy"))
    description = models.TextField(max_length=255, blank=False, null=False, verbose_name=_("Opis"))
    note = models.TextField(max_length=255, blank=False, null=False, verbose_name=_("Uwagi"))
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    cost = models.FloatField(default=0.0, blank=False, null=False, verbose_name=_('Szacunkowy koszt'))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("Klient"))
    hardware_model = models.ForeignKey(HardwareModel, on_delete=models.CASCADE, verbose_name=_("Model"))
    hardware_type = models.ForeignKey(HardwareType, on_delete=models.CASCADE, verbose_name=_("Rodzaj sprzętu"))

    def __str__(self):
        return f'{self.client}'

    class Meta:
        verbose_name_plural = _("Naprawy")
        verbose_name = _("Naprawa")
