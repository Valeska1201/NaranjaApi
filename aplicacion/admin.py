from django.contrib import admin
from aplicacion.models import Postre

class PostreAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']

# Register your models here.
admin.site.register(Postre, PostreAdmin)