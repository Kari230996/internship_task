import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

import django
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def create_tokens():
    users = User.objects.all()

    for user in users:
        token, created = Token.objects.get_or_create(user=user)
        if created:
            print(f"Token created for user {user.username}: {token.key}")
        else:
            print(f"Token already exists for user {user.username}: {token.key}")

if __name__ == "__main__":
    create_tokens()
