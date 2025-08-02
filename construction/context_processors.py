from django.conf import settings
from django.utils import translation


def language_context(request):
    """
    Context processor to provide language-related variables to all templates.
    """
    current_language = translation.get_language()
    return {
        'current_language': current_language,
        'LANGUAGE_CODE': current_language,  # Ensure LANGUAGE_CODE is available
        'available_languages': settings.LANGUAGES,
        'is_rtl': current_language == 'fa',
        'LANGUAGES': settings.LANGUAGES,  # Add this for completeness
    } 