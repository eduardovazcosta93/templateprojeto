from django.contrib import admin
from .models import Register
# Register your models here.


class ModelAdmin(admin.ModelAdmin):
    ...


admin.site.register(Register, ModelAdmin)
