# Install the apps from your project.
INSTALLED_APPS += [
    'blog',
    'profile',
]

# Modify existing settings.
TEMPLATES[0]['OPTIONS']['context_processors'].append('my_processor')
MIDDLEWARE.append('my_middleware']

# Add any new project-specific settings.
USERNAME_BASE_URL = '^(?P<username>[^\]+)/'
