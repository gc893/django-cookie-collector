from django.contrib import admin
from .models import Cookie, Batch, Ingredient

# Register your models here
admin.site.register(Cookie)
admin.site.register(Batch)
admin.site.register(Ingredient)