from django.contrib import admin

# Register your models here.

from containers.models import Container
@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    pass
