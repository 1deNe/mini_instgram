# hello/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken as JWTRefreshToken
import datetime  # <- осыны қостық

@receiver(post_save, sender=User)
def create_refresh_token_for_new_user(sender, instance, created, **kwargs):
    if created:
        refresh = JWTRefreshToken.for_user(instance)
        jti = str(refresh['jti'])
        # UTC timezone қолдану
        expires_at = datetime.datetime.fromtimestamp(
            refresh['exp'], tz=datetime.timezone.utc
        )

        RefreshToken.objects.create(
            user=instance,
            jti=jti,
            revoked=False,
            expires_at=expires_at
        )