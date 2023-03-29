from django.db import models
from django.utils.translation import ugettext_lazy as _

HADRWARE_STATUS = [
    (0, _('Nowy')),
    (1, _('Używany')),
    (2, _('Uszkodzony')),
]

SYSTEM = [
    (0, _('Brak')),
    (1, _('Android')),
    (2, _('iOS')),
    (3, _('Windows')),
    (4, _('Niestandardowy')),
]


class HardwareType(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name=_("Nazwa"))

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'hardware'
        verbose_name_plural = _("Rodzaj sprzętu")
        verbose_name = _("Rodzaje sprzętu")


class HardwareBrand(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name=_("Nazwa"))

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'hardware'
        verbose_name_plural = _("Marka")
        verbose_name = _("Marki")


class HardwareModel(models.Model):
    model = models.CharField(max_length=30, blank=False, null=False, verbose_name=_("Model"))
    brand = models.ForeignKey(HardwareBrand, on_delete=models.CASCADE, null=False, verbose_name=_("Marka"))
    imei1 = models.CharField(max_length=16, blank=True, null=True, verbose_name=_("IMEI1"))
    imei2 = models.CharField(max_length=16, blank=True, null=True, verbose_name=_("IMEI2"))
    type = models.ForeignKey(HardwareType, on_delete=models.CASCADE, null=False, verbose_name=_("Rodzaj"))
    description = models.TextField(max_length=255, blank=False, null=False, verbose_name=_("Opis"))
    ram = models.CharField(max_length=8, blank=True, null=True, verbose_name=_("Pamięć RAM"))
    storage = models.CharField(max_length=8, blank=True, null=True, verbose_name=_("Pamięć wbudowana"))
    op_system = models.IntegerField(default=0, choices=SYSTEM, verbose_name=_("System operacyjny"))
    state = models.IntegerField(default=0, choices=HADRWARE_STATUS, verbose_name=_("Stan techniczny"))

    def __str__(self):
        return f'{self.model}'

    class Meta:
        app_label = 'hardware'
        verbose_name_plural = _("Model")
        verbose_name = _("Modele")
