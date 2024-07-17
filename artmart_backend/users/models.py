from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, TextField, DateTimeField

from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for artmart_backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # # First and last name do not cover name patterns around the globe
    # name = CharField(_("Name of User"), blank=True, max_length=255)
    # first_name = None  # type: ignore[assignment]
    # last_name = None  # type: ignore[assignment]
    # email = EmailField(_("email address"), unique=True)
    # username = None  # type: ignore[assignment]

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
    username = None  # type: ignore[assignment]
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = EmailField(_("email address"), unique=True)
    
    phone_number=CharField(_("phone_number"), max_length=255,null=True)
    user_role = CharField(
        _("user role"),
        max_length=50,
        choices=[("ADMIN", "Admin"), ("SELLER", "Seller"), ("BUYER", "Buyer")],
    )
   
    registration_date = DateTimeField(_("registration date"), auto_now_add=True)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
