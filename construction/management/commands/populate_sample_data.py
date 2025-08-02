from django.core.management.base import BaseCommand
from django.utils import timezone
from construction.models import Project, Team, Blog, CompanyInfo
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with sample data for the construction website'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create Company Info
        company_info, created = CompanyInfo.objects.get_or_create(
            name="Dorsamehr Construction",
            defaults={
                'tagline': "Building Excellence, Creating Value",
                'description': "Dorsamehr Construction is a leading construction company with over 15 years of experience in delivering exceptional quality projects across residential, commercial, and industrial sectors. We are committed to innovation, sustainability, and customer satisfaction.",
                'address': "123 Construction Street, Tehran, Iran 12345",
                'phone': "+98 21 1234 5678",
                'email': "info@dorsamehr.com",
                'website': "https://dorsamehr.com",
                'years_experience': 15,
                'projects_completed': 200,
                'team_members': 50,
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created company info'))
        
        # Create Team Members
        team_members_data = [
            {
                'name': 'Ahmad Rezaei',
                'position': 'architect',
                'bio': 'Senior architect with 12 years of experience in residential and commercial design. Specializes in sustainable architecture and modern design principles.',
                'email': 'ahmad@dorsamehr.com',
                'phone': '+98 21 1234 5679',
                'experience_years': 12,
            },
            {
                'name': 'Sara Mohammadi',
                'position': 'engineer',
                'bio': 'Structural engineer with expertise in seismic design and innovative construction techniques. Has worked on numerous high-rise projects.',
                'email': 'sara@dorsamehr.com',
                'phone': '+98 21 1234 5680',
                'experience_years': 10,
            },
            {
                'name': 'Mohammad Karimi',
                'position': 'project_manager',
                'bio': 'Experienced project manager with a track record of delivering complex projects on time and within budget. Strong leadership and communication skills.',
                'email': 'mohammad@dorsamehr.com',
                'phone': '+98 21 1234 5681',
                'experience_years': 15,
            },
            {
                'name': 'Fatemeh Ahmadi',
                'position': 'designer',
                'bio': 'Interior designer with a passion for creating functional and beautiful spaces. Specializes in modern and minimalist design.',
                'email': 'fatemeh@dorsamehr.com',
                'phone': '+98 21 1234 5682',
                'experience_years': 8,
            },
        ]
        
        for member_data in team_members_data:
            member, created = Team.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            if created:
                self.stdout.write(f'Created team member: {member.name}')
        
        # Create Projects
        projects_data = [
            {
                'title': 'Modern Office Complex',
                'description': 'A state-of-the-art office complex featuring sustainable design, smart building technology, and modern amenities. The project includes 15 floors of office space, conference facilities, and a rooftop garden.',
                'project_type': 'commercial',
                'location': 'Tehran, Iran',
                'area': '25,000 sq ft',
                'completion_date': date(2023, 12, 15),
                'featured': True,
            },
            {
                'title': 'Luxury Residential Tower',
                'description': 'Premium residential development with 50 luxury apartments, featuring high-end finishes, smart home technology, and panoramic city views. Includes amenities like gym, pool, and concierge services.',
                'project_type': 'residential',
                'location': 'Tehran, Iran',
                'area': '35,000 sq ft',
                'completion_date': date(2023, 8, 20),
                'featured': True,
            },
            {
                'title': 'Industrial Manufacturing Facility',
                'description': 'Large-scale manufacturing facility designed for efficiency and productivity. Features advanced automation systems, sustainable energy solutions, and worker safety protocols.',
                'project_type': 'industrial',
                'location': 'Isfahan, Iran',
                'area': '100,000 sq ft',
                'completion_date': date(2023, 6, 10),
                'featured': True,
            },
            {
                'title': 'Shopping Mall Renovation',
                'description': 'Complete renovation of an existing shopping mall, modernizing the interior design, improving energy efficiency, and enhancing the customer experience.',
                'project_type': 'commercial',
                'location': 'Mashhad, Iran',
                'area': '45,000 sq ft',
                'completion_date': date(2023, 10, 5),
                'featured': False,
            },
            {
                'title': 'Sustainable Housing Community',
                'description': 'Eco-friendly residential community featuring solar panels, rainwater harvesting, and green building materials. Designed for modern families with a focus on sustainability.',
                'project_type': 'residential',
                'location': 'Shiraz, Iran',
                'area': '60,000 sq ft',
                'completion_date': date(2023, 9, 15),
                'featured': False,
            },
            {
                'title': 'Highway Bridge Construction',
                'description': 'Major infrastructure project involving the construction of a modern highway bridge with advanced engineering solutions for durability and safety.',
                'project_type': 'infrastructure',
                'location': 'Tabriz, Iran',
                'area': '2,000 sq ft',
                'completion_date': date(2023, 7, 30),
                'featured': False,
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created project: {project.title}')
        
        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'The Future of Sustainable Construction',
                'slug': 'future-sustainable-construction',
                'content': 'Sustainable construction is no longer just a trend—it\'s becoming the standard in the industry. As we move towards a more environmentally conscious future, construction companies are adopting green building practices that not only benefit the planet but also provide long-term value to clients. Key trends in sustainable construction include: Green Building Materials, Energy Efficiency, Renewable Energy Integration, Water Conservation, and Smart Building Technology. At Dorsamehr Construction, we\'re committed to implementing these sustainable practices in all our projects.',
                'excerpt': 'Explore the latest trends in sustainable construction and how they are shaping the future of the industry.',
                'author': 'Ahmad Rezaei',
                'published_date': timezone.now(),
                'tags': 'sustainability, green building, construction trends',
            },
            {
                'title': 'Essential Safety Protocols for Construction Sites',
                'slug': 'construction-safety-protocols',
                'content': 'Safety is the cornerstone of any successful construction project. At Dorsamehr Construction, we prioritize the safety of our workers, clients, and the public above all else. Essential safety protocols include Personal Protective Equipment (PPE), regular safety training, daily safety meetings, proper signage, equipment maintenance, and emergency procedures. We also implement hazard identification and control measures, clear communication channels, and modern technology for safety monitoring.',
                'excerpt': 'Learn about the essential safety protocols that every construction site should implement to protect workers and ensure project success.',
                'author': 'Mohammad Karimi',
                'published_date': timezone.now(),
                'tags': 'safety, construction protocols, workplace safety',
            },
            {
                'title': 'Modern Construction Technologies Transforming the Industry',
                'slug': 'modern-construction-technologies',
                'content': 'The construction industry is undergoing a technological revolution that\'s changing how we design, plan, and build projects. From 3D printing to artificial intelligence, these innovations are making construction faster, safer, and more efficient. Key technologies include Building Information Modeling (BIM), 3D printing, drones and aerial imaging, artificial intelligence and machine learning, virtual and augmented reality, robotics and automation, and sustainable technologies. At Dorsamehr Construction, we\'re actively incorporating these technologies into our projects.',
                'excerpt': 'Discover how cutting-edge technologies are revolutionizing the construction industry and improving project outcomes.',
                'author': 'Sara Mohammadi',
                'published_date': timezone.now(),
                'tags': 'technology, innovation, construction trends, BIM',
            },
        ]
        
        for blog_data in blog_posts_data:
            blog, created = Blog.objects.get_or_create(
                slug=blog_data['slug'],
                defaults=blog_data
            )
            if created:
                self.stdout.write(f'Created blog post: {blog.title}')
        
        self.stdout.write(self.style.SUCCESS('Successfully created sample data!'))
        self.stdout.write('You can now run the development server and visit the website.') 