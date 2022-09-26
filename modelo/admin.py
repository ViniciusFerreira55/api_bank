from django.contrib import admin
from . import models

class imagens_display(admin.ModelAdmin):
    list_display = ('id', 'titulo')
admin.site.register(models.Imagens)
