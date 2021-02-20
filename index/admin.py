from django.contrib import admin
# Register your models here.

from .models import SlideInfo, Logo, SaleFutures, Subscriber

admin.site.register(SlideInfo)
admin.site.register(Logo)
admin.site.register(SaleFutures)
admin.site.register(Subscriber)
