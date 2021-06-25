from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doc)
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Supply)
admin.site.register(Material)
