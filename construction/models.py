from django.db import models
from django.utils import timezone

class Project(models.Model):
    PROJECT_TYPES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('industrial', 'Industrial'),
        ('infrastructure', 'Infrastructure'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    location = models.CharField(max_length=200)
    area = models.CharField(max_length=100, help_text="e.g., 5000 sq ft")
    completion_date = models.DateField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-completion_date']

class Team(models.Model):
    POSITIONS = [
        ('architect', 'Architect'),
        ('engineer', 'Engineer'),
        ('project_manager', 'Project Manager'),
        ('foreman', 'Foreman'),
        ('worker', 'Worker'),
        ('designer', 'Designer'),
    ]
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20, choices=POSITIONS)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='company/', blank=True, null=True)
    about_image = models.ImageField(upload_to='company/', blank=True, null=True)
    years_experience = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)
    team_members = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Company Info"
