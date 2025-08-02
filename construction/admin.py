from django.contrib import admin
from .models import Project, Team, Blog, Contact, CompanyInfo

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'location', 'completion_date', 'featured', 'created_at']
    list_filter = ['project_type', 'featured', 'completion_date', 'created_at']
    search_fields = ['title', 'description', 'location']
    list_editable = ['featured']
    date_hierarchy = 'completion_date'

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience_years', 'email', 'is_active']
    list_filter = ['position', 'is_active', 'experience_years']
    search_fields = ['name', 'bio', 'email']
    list_editable = ['is_active']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'is_published']
    list_filter = ['is_published', 'published_date']
    search_fields = ['title', 'content', 'author']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'years_experience', 'projects_completed']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'description')
        }),
        ('Contact Information', {
            'fields': ('address', 'phone', 'email', 'website')
        }),
        ('Media', {
            'fields': ('logo', 'hero_image', 'about_image')
        }),
        ('Statistics', {
            'fields': ('years_experience', 'projects_completed', 'team_members')
        }),
    )
