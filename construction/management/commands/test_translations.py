from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _
from django.utils.translation import activate
from django.conf import settings

class Command(BaseCommand):
    help = 'Test the translation system'

    def handle(self, *args, **options):
        self.stdout.write("=== Translation System Test ===")
        self.stdout.write(f"Available languages: {settings.LANGUAGES}")
        self.stdout.write(f"Default language: {settings.LANGUAGE_CODE}")
        self.stdout.write(f"Locale paths: {settings.LOCALE_PATHS}")
        
        # Test English
        activate('en')
        self.stdout.write("\n=== English Translations ===")
        self.stdout.write(_("About Us - Dorsamehr Construction"))
        self.stdout.write(_("Our Story"))
        self.stdout.write(_("Quality Excellence"))
        self.stdout.write(_("Get In Touch"))
        
        # Test Persian (will show English if translations not loaded)
        activate('fa')
        self.stdout.write("\n=== Persian Translations ===")
        self.stdout.write(_("About Us - Dorsamehr Construction"))
        self.stdout.write(_("Our Story"))
        self.stdout.write(_("Quality Excellence"))
        self.stdout.write(_("Get In Touch"))
        
        self.stdout.write("\n")
        self.stdout.write(self.style.SUCCESS('Translation test completed!'))
        self.stdout.write(self.style.WARNING('Note: Persian translations may show English text if .mo files are not compiled.')) 