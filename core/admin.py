from django.contrib import admin
from core.models import UserApp


class ListingUsers(admin.ModelAdmin):
    list_display = ('id', 'fullname')


admin.site.register(UserApp, ListingUsers)
