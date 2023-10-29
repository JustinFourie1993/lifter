import os
import sys


def main():
    """Run administrative tasks."""

    # Set the DJANGO_SETTINGS_MODULE environment variable to specify the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tables.settings')

    try:
        # Try to import the execute_from_command_line function from Django's core management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle ImportError by providing a clear error message
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the Django management commands specified in sys.argv
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Call the main function if this script is executed directly
    main()
