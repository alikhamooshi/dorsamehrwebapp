# Dorsamehr Construction Website

A professional construction company website built with Django 5.2.4 and Tailwind CSS. This website showcases the company's projects, team, services, and provides a platform for client communication.

## Features

- **Modern Design**: Professional and responsive design using Tailwind CSS
- **Project Portfolio**: Showcase construction projects with filtering and search
- **Team Management**: Display team members with their expertise and contact information
- **Blog System**: Share industry insights and company updates
- **Contact Form**: Easy client communication with form validation
- **Admin Panel**: Full Django admin interface for content management
- **Responsive**: Mobile-friendly design that works on all devices

## Pages

1. **Home**: Hero section, services overview, featured projects, company stats
2. **About**: Company story, values, mission, vision, and team overview
3. **Projects**: Portfolio with filtering by project type and search functionality
4. **Team**: Detailed team member profiles organized by position
5. **Blog**: Articles with search and pagination
6. **Contact**: Contact form and company information

## Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Tailwind CSS (CDN)
- **Icons**: Font Awesome
- **Database**: SQLite (default)

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd dorsamehrwebapp
```

### Step 2: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install django==5.2.4
```

### Step 5: Run Migrations

```bash
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 7: Populate Sample Data

```bash
python manage.py populate_sample_data
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

The website will be available at `http://127.0.0.1:8000/`

## Admin Access

- **URL**: `http://127.0.0.1:8000/admin/`
- **Username**: admin (or the one you created)
- **Password**: (the one you set during superuser creation)

## Project Structure

```
dorsamehrwebapp/
├── construction/                 # Main Django app
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── urls.py                  # URL patterns
│   ├── admin.py                 # Admin configuration
│   ├── forms.py                 # Form definitions
│   └── management/              # Management commands
│       └── commands/
│           └── populate_sample_data.py
├── dorsamehrkish/               # Django project settings
│   ├── settings.py              # Project settings
│   └── urls.py                  # Main URL configuration
├── templates/                   # HTML templates
│   ├── base.html               # Base template
│   └── construction/           # App-specific templates
│       ├── home.html
│       ├── about.html
│       ├── contact.html
│       ├── team.html
│       ├── projects.html
│       ├── project_detail.html
│       ├── blog.html
│       └── blog_detail.html
├── static/                      # Static files
├── media/                       # User-uploaded files
├── manage.py                    # Django management script
└── README.md                    # This file
```

## Models

### Project
- Title, description, project type
- Location, area, completion date
- Featured flag, image upload

### Team
- Name, position, bio
- Contact information, experience
- Image upload, LinkedIn profile

### Blog
- Title, content, excerpt
- Author, publication date
- Tags, image upload

### Contact
- Name, email, phone
- Subject, message
- Timestamp, read status

### CompanyInfo
- Company details and statistics
- Contact information
- Logo and hero images

## Customization

### Adding New Projects
1. Go to Django admin panel
2. Navigate to "Projects" section
3. Click "Add Project"
4. Fill in project details
5. Save the project

### Adding Team Members
1. Go to Django admin panel
2. Navigate to "Teams" section
3. Click "Add Team"
4. Fill in member details
5. Save the team member

### Adding Blog Posts
1. Go to Django admin panel
2. Navigate to "Blogs" section
3. Click "Add Blog"
4. Write your content
5. Set publication date and tags
6. Save the blog post

### Updating Company Information
1. Go to Django admin panel
2. Navigate to "Company Info" section
3. Edit the company details
4. Save changes

## Features to Add

- **Image Gallery**: Multiple images per project
- **Testimonials**: Client feedback system
- **Newsletter**: Email subscription functionality
- **Online Quote Calculator**: Project estimation tool
- **Multi-language Support**: Internationalization
- **SEO Optimization**: Meta tags and sitemap
- **Analytics Integration**: Google Analytics
- **Social Media Integration**: Social sharing buttons

## Deployment

### Production Settings

For production deployment, update the following in `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Configure your production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configure static files
STATIC_ROOT = '/path/to/your/static/files/'
MEDIA_ROOT = '/path/to/your/media/files/'
```

### Recommended Hosting Platforms

- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS with full control
- **AWS**: Scalable cloud hosting
- **Vercel**: Fast static hosting with serverless functions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please contact:
- Email: info@dorsamehr.com
- Phone: +98 21 1234 5678

## Credits

- **Django**: Web framework
- **Tailwind CSS**: Styling framework
- **Font Awesome**: Icons
- **Design**: Professional construction company website template

---

**Dorsamehr Construction** - Building Excellence, Creating Value
