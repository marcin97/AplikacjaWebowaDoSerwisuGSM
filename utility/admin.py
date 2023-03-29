from django.contrib import admin

from utility.models import Invoice, Part


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    fields = ('client', 'cost', ('sold_at', 'due_at'), 'nip', ('city', 'address', 'post_code'), 'payment_type')
    list_display = ('doc_number', 'sold_at', 'due_at', 'nip', 'cost', 'payment_type',)
    search_fields = ('doc_number', 'sold_at', 'due_at', 'nip', 'payment_type',)
    list_filter = ('payment_type',)

    def sold_at(self, obj):
        return obj.created_at.strftime("%d-%m-%Y")

    def due_at(self, obj):
        return obj.due_at.strftime("%d-%m-%Y")


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    fields = (('hardware_model', 'hardware_type'), 'type', 'signature', 'description', 'stock')
    list_display = ('name', 'type', 'signature', 'stock', 'item')
    search_fields = ('name', 'type', 'signature', 'stock', 'item', 'hardware_type', 'hardware_model')
    list_filter = ('stock', 'hardware_model', 'hardware_type')

    def sold_at(self, obj):
        return obj.created_at.strftime("%d-%m-%Y")

    def due_at(self, obj):
        return obj.due_at.strftime("%d-%m-%Y")

    def item(self, obj):
        return f'{obj.hardware_model.brand.name}: {obj.hardware_model}'
