from django.contrib import admin
from .models import Trigger,Suggestion,JournalEntry
# Register your models here.

admin.site.register(Trigger)
admin.site.register(Suggestion)
admin.site.register(JournalEntry)
