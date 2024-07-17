# your_app/signals.py

from django.dispatch import receiver
from allauth.account.signals import email_confirmed
from django.shortcuts import redirect
from django.conf import settings

@receiver(email_confirmed)
def user_signed_up(request, email_address, **kwargs):
    user = email_address.user
    if user.user_role == 'SELLER':
        # Redirect to the artist registration form (step 1)
        return redirect('artist_wizard_step1')
