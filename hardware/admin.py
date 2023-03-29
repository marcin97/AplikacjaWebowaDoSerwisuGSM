from django.contrib import admin

from hardware.models import HardwareType, HardwareBrand, HardwareModel


@admin.register(HardwareType)
class HardwareTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(HardwareBrand)
class HardwareBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(HardwareModel)
class HardwareModelAdmin(admin.ModelAdmin):
    fields = (('model', 'brand', 'type'), ('imei1', 'imei2'), 'description', ('ram', 'storage'), 'state')
    list_display = ('brand', 'model', 'type', 'state')
    search_fields = ('brand__name', 'model', 'type__name')
    list_filter = ('state', 'op_system', 'type')
