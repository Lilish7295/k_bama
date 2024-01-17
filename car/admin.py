from django.contrib.admin import ModelAdmin,register
from .models import Car


@register(Car)
class CarAdmin(ModelAdmin):
    pass






