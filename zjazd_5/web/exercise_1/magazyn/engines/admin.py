# Register your models here.



from django.contrib import admin
from engines.models import Engine


# Register your models here.


class EngineAdmin(admin.ModelAdmin):
    # list_display = ['pojemnosc', 'id', 'ilosc_cylindrow', 'cykl_spalania']
    # search_fields = ['pojemnosc', 'ilosc_cylindrow', 'cykl_spalania']
    # list_filter = ['ilosc_cylindrow']
    pass


admin.site.register(Engine, EngineAdmin)

