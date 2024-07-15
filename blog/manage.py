#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
DEBUG = os.environ.get("DEBUG")
# if not DEBUG:
#     DEBUG = False
# from blog.settings.base import DEBUG


# def main():
#     """Run administrative tasks."""
#     if DEBUG:
#         os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.local')
#         print('running from Debug')
#     else:
#         os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.production')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)

def main():
    """Run administrative tasks."""

    if DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.local')
        print('running from Debug')
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
