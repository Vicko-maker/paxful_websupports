# login/signals.py
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_superuser(sender, **kwargs):
    if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
        User.objects.create_superuser(
            username=settings.SUPERUSER_USERNAME,
            email=settings.SUPERUSER_EMAIL,
            password=settings.SUPERUSER_PASSWORD
        )
        print(f'Superuser {settings.SUPERUSER_USERNAME} created.')
    else:
        print(f'Superuser {settings.SUPERUSER_USERNAME} already exists.')
