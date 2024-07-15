#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from blog.settings import base
# from dotenv import load_dotenv
# load_dotenv()

# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
# DEBUG = True
# DEBUG = os.environ.get("DEBUG")


def main():
    """Run administrative tasks."""

    if base.DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.local')
        print('running from Debug', base.DEBUG)
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
