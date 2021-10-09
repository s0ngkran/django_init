from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('updated_on','user')
    def get_ordering(self, request):
        return ['-updated_on']

admin.site.register(Profile, ProfileAdmin)

admin.site.register(UserImage)