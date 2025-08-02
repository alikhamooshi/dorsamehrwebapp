# Bilingual System Setup - Dorsamehr Construction

## Overview
The Dorsamehr Construction website now supports two languages:
- **English** (en) - Default language
- **Persian** (fa) - فارسی

## Features Implemented

### 1. Language Configuration
- ✅ Django internationalization enabled
- ✅ Persian and English language support
- ✅ Locale middleware configured
- ✅ Language prefix URLs (e.g., `/fa/about/`, `/en/about/`)

### 2. Language Switcher
- ✅ Desktop dropdown language switcher in navigation
- ✅ Mobile language switcher in mobile menu
- ✅ Language preference saved in cookies
- ✅ Automatic language detection

### 3. Translation System
- ✅ Translation files created (`locale/fa/LC_MESSAGES/django.po`)
- ✅ All text strings marked for translation
- ✅ Persian translations for all content
- ✅ RTL (Right-to-Left) support for Persian

### 4. Template Updates
- ✅ Base template with language switcher
- ✅ About page fully translated
- ✅ Navigation menu translated
- ✅ Footer translated

## How to Use

### For Users
1. **Desktop**: Click the "Language" dropdown in the navigation bar
2. **Mobile**: Open mobile menu and scroll to language section
3. **Select**: Choose between English (انگلیسی) or Persian (فارسی)
4. **Browse**: The entire website will switch to the selected language

### For Developers

#### Adding New Translations
1. Add `{% load i18n %}` to your template
2. Wrap text in `{% trans "Your text here" %}`
3. Add translation to `locale/fa/LC_MESSAGES/django.po`
4. Compile translations (see below)

#### Compiling Translations (Windows)
Since gettext tools aren't available on Windows, use this workaround:

```bash
# Install polib
pip install polib

# Run the compilation script
python compile_translations.py
```

#### Testing Translations
```bash
python manage.py test_translations
```

## URL Structure
- English: `/about/` (default)
- Persian: `/fa/about/`
- Language switcher: `/set-language/`

## Files Modified
- `dorsamehrkish/settings.py` - Internationalization settings
- `dorsamehrkish/urls.py` - Language prefix URLs
- `construction/views.py` - Language switcher view
- `construction/urls.py` - Language switcher URL
- `templates/base.html` - Language switcher UI
- `templates/construction/about.html` - Translation tags
- `locale/fa/LC_MESSAGES/django.po` - Persian translations

## Next Steps
1. Add translations to remaining templates (home, contact, projects, team, blog)
2. Compile .mo files for production
3. Add Persian content for blog posts and projects
4. Test RTL layout thoroughly
5. Add Persian date/time formatting

## Notes
- Persian translations are currently in .po format
- .mo files need to be compiled for production use
- RTL support is automatically enabled for Persian
- Language preference is saved in browser cookies 