from django.contrib import admin
from .models import Thought

class ThoughtAdmin(admin.ModelAdmin):
    list_display = ("name", "content","likes", "date")

admin.site.register(Thought, ThoughtAdmin)