from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('datetime','user')
    def get_ordering(self, request):
        return ['-datetime']

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Hand)