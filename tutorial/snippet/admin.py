from django.contrib import admin
from .models import Snippet

# Register your models here.
@admin.register(Snippet)
class UserAmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'language', 'owner', 'created']
    list_filter = []
    list_per_page = 10

    actions_on_top = False
    actions_on_bottom = True

    pass