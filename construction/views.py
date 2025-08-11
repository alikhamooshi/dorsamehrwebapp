from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import translation
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from .models import Project, Team, Blog, Contact, CompanyInfo
from .forms import ContactForm

def home(request):
    """Home page view with featured projects and company stats"""
    try:
        company_info = CompanyInfo.objects.first()
    except:
        company_info = None
    
    featured_projects = Project.objects.filter(featured=True)[:6]
    recent_projects = Project.objects.all()[:3]
    team_members = Team.objects.filter(is_active=True)[:4]
    recent_blogs = Blog.objects.filter(is_published=True)[:3]
    
    context = {
        'company_info': company_info,
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
        'team_members': team_members,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'construction/home.html', context)

def about(request):
    """About us page view"""
    try:
        company_info = CompanyInfo.objects.first()
    except:
        company_info = None
    
    team_members = Team.objects.filter(is_active=True)
    
    context = {
        'company_info': company_info,
        'team_members': team_members,
    }
    return render(request, 'construction/about.html', context)

def contact(request):
    """Contact page view with contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    try:
        company_info = CompanyInfo.objects.first()
    except:
        company_info = None
    
    context = {
        'form': form,
        'company_info': company_info,
    }
    return render(request, 'construction/contact.html', context)

def team(request):
    """Team page view with all team members"""
    team_members = Team.objects.filter(is_active=True)
    
    # Group by position
    positions = {}
    for member in team_members:
        position = member.get_position_display()
        if position not in positions:
            positions[position] = []
        positions[position].append(member)
    
    context = {
        'team_members': team_members,
        'positions': positions,
    }
    return render(request, 'construction/team.html', context)

def team_employment(request):
    """Employment opportunities page"""
    try:
        company_info = CompanyInfo.objects.first()
    except:
        company_info = None
    
    context = {
        'company_info': company_info,
    }
    return render(request, 'construction/team_employment.html', context)

def team_partnership(request):
    """Partnership opportunities page"""
    try:
        company_info = CompanyInfo.objects.first()
    except:
        company_info = None
    
    context = {
        'company_info': company_info,
    }
    return render(request, 'construction/team_partnership.html', context)

def team_barter(request):
    """Barter/Exchange opportunities page"""
    try:
        company_info = CompanyInfo.objects.first()
    except:
        company_info = None
    
    context = {
        'company_info': company_info,
    }
    return render(request, 'construction/team_barter.html', context)

def projects(request):
    """Projects portfolio page"""
    projects_list = Project.objects.all()
    
    # Filter by project type
    project_type = request.GET.get('type')
    if project_type:
        projects_list = projects_list.filter(project_type=project_type)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        projects_list = projects_list.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(projects_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'project_types': Project.PROJECT_TYPES,
        'current_type': project_type,
        'search_query': search_query,
    }
    return render(request, 'construction/projects.html', context)

def project_detail(request, project_id):
    """Individual project detail page"""
    project = get_object_or_404(Project, id=project_id)
    related_projects = Project.objects.filter(project_type=project.project_type).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'construction/project_detail.html', context)

def blog(request):
    """Blog listing page"""
    blogs = Blog.objects.filter(is_published=True)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        blogs = blogs.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'construction/blog.html', context)

def blog_detail(request, slug):
    """Individual blog post detail page"""
    blog_post = get_object_or_404(Blog, slug=slug, is_published=True)
    recent_blogs = Blog.objects.filter(is_published=True).exclude(id=blog_post.id)[:3]
    
    context = {
        'blog_post': blog_post,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'construction/blog_detail.html', context)

def gallery(request):
    """Project gallery page"""
    return render(request, 'construction/gallery.html')

def debug_language(request):
    """Debug view for language switching"""
    return render(request, 'debug_language.html')
