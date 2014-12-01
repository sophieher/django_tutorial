from django.contrib import admin
from food_mood.models import Entry, UserProfile

admin.site.register(Entry)
admin.site.register(UserProfile)

class EntryAdmin(admin.ModelAdmin):
    exclude = ('eater',)
    list_display = ('pub_date', 'food', 'mood', 'eater')