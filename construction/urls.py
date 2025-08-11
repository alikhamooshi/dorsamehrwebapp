from django.urls import path
from . import views

app_name = 'construction'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('team/employment/', views.team_employment, name='team_employment'),
    path('team/partnership/', views.team_partnership, name='team_partnership'),
    path('team/barter/', views.team_barter, name='team_barter'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('debug-language/', views.debug_language, name='debug_language'),
] 