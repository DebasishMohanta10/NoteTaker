from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("short_note","updated_at")
    search_fields = ("content",)
    list_filter = ("created_at",)

admin.site.register(Note,NoteAdmin)