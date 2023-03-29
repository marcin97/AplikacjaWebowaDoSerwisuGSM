from django.contrib import admin

from main.forms import PhoneForm
from main.models import Client, Repair


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    fields = ('client', ('hardware_type', 'hardware_model'), ('description', 'note'), 'repair_status', 'cost')
    list_display = ('id', 'display_date', 'client', 'get_mail', 'get_phone_number', 'hardware_model', 'hardware_type',
                    'cost', 'repair_status')
    search_fields = ('client__first_name', 'client__last_name', 'client__mail',
                     'client__phone_number', 'hardware_model__model', 'hardware_type__name')
    list_filter = ('repair_status',)

    def get_mail(self, obj):
        return obj.client.mail

    get_mail.short_description = 'Mail'

    def get_phone_number(self, obj):
        return obj.client.phone_number

    get_phone_number.short_description = 'Phone number'

    def display_date(self, obj):
        return obj.created_at.strftime("%d-%m-%Y")

    @admin.action(description='Generate PDF')
    def generatePDF(modeladmin, request, queryset):
        url = 'templates/admin/repair/?pks=' + ','.join(str([q.pk for q in queryset]))

    actions = [generatePDF]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), ('mail', 'phone_number'), 'note')
    list_display = ('first_name', 'last_name', 'mail', 'phone_number')
    search_fields = ('first_name', 'last_name', 'mail',
                     'phone_number')
    form = PhoneForm
