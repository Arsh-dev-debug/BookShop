import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

# Force HTTP in development
os.environ["HTTPS"] = "off"

# Custom WSGI application
def application(environ, start_response):
    # Force HTTP
    environ['wsgi.url_scheme'] = 'http'
    
    # Get the original application
    django_app = get_wsgi_application()
    
    # Call the original application
    return django_app(environ, start_response)
