from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Experience, Project, Achievement, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_available', 'photo_preview']
    readonly_fields = ['photo_preview']

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:50%;object-fit:cover">', obj.photo.url)
        return "No photo"
    photo_preview.short_description = "Photo"

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'show_in_pills', 'order']
    list_editable = ['percentage', 'order', 'show_in_pills']
    ordering = ['order']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'type', 'period', 'order']
    list_editable = ['order']
    list_filter = ['type']
    ordering = ['order']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'emoji', 'is_featured', 'order', 'live_url']
    list_editable = ['is_featured', 'order']
    ordering = ['order']

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'meta', 'order']
    list_editable = ['order']
    ordering = ['order']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'sent_at', 'is_read']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'sent_at']
    list_filter = ['is_read']

    def has_add_permission(self, request):
        return False

admin.site.site_header = "Shivani Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Dashboard"
