from django.contrib import admin

from bw.models import ContactModel, User, siteDataModel

# Register your models here.
admin.site.register(User)
admin.site.register(ContactModel)
admin.site.register(siteDataModel)

