import os
import sys
import django
from django.contrib.auth import get_user_model
import psycopg
from psycopg import OperationalError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.local')
django.setup()


def test_db_connection():
    try:
        connection = psycopg.connect(
            dbname="railway",
            user="postgres",
            password="lKmLfPjlbJxpTMzPTAiLPhzNnIBLFABV",
            host="viaduct.proxy.rlwy.net",
            port="32281",
        )
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        sys.exit(1)


def create_superuser(username, email, password):
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'Superuser {username} created successfully.')
    else:
        print(f'Superuser {username} already exists.')


if __name__ == "__main__":
    # Test database connection
    test_db_connection()

    # Create superuser
    username = 'ssanger'
    email = 'ssanger2020@gmail.com'
    password = 'Th3r315@houseInNewOrleans'
    create_superuser(username, email, password)