#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # Append the parent directory of `bookstore` to the PYTHONPATH
    sys.path.append(os.path.join(os.path.dirname(__file__), 'BookShop'))
    
    # Set DJANGO_SETTINGS_MODULE to the correct settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
