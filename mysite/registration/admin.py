from django.contrib import admin

from .models import Company, User, Event, UserEvent, BuildUserInformation
# Register your models here.
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(UserEvent)
admin.site.register(BuildUserInformation)