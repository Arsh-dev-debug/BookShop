import os
import sys
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    # Set development settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    
    # Force HTTP in development
    os.environ["HTTPS"] = "off"
    
    # Get port from command line or use default
    port = sys.argv[1] if len(sys.argv) > 1 else "8000"
    
    # Run the development server with explicit HTTP
    execute_from_command_line([
        "manage.py", 
        "runserver", 
        f"127.0.0.1:{port}",
        "--noreload",
        "--insecure"
    ]) 