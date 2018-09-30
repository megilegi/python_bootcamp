
# Register your models here.


from django.contrib import admin
from cars.models import Car


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    # list_display = ['marka', 'id', 'rok_produckji', 'typ_nadwozia']
    # search_fields = ['marka', 'rok_produckji', 'typ_nadwozia']
    # list_filter = ['rok_produkcji']
    pass


admin.site.register(Car, CarAdmin)
