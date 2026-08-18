from django.contrib import admin

from .models import Achievement, Certificate, ContactMessage, Education, Profile, Project, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'github_url', 'demo_url')
    search_fields = ('title', 'technologies')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'proficiency')
    list_filter = ('category',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'issued_by')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'location', 'year_range')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'email_sent')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at', 'email_sent', 'email_error')
    ordering = ('-created_at',)
