from django.contrib.auth.models import User
from .models import Feedback, Property, Document
from django.contrib import admin

from .models import Announcement

admin.site.register(Feedback)
admin.site.register(Property)
admin.site.register(Announcement)
admin.site.register(Document)




class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['subject', 'homeowner', 'created_at']
    fields = ['subject', 'homeowner', 'feedback_text']

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'date_posted')
    search_fields = ('subject', 'author__username')
    list_filter = ('date_posted',)
