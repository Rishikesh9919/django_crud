from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField


def validate_age(value):
    if (datetime.now().date() - value).days < 18 * 365:
        raise ValidationError("Must be at least 18 years old.")


class UserProfile(models.Model):
    GENDER_CONST = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CONST)
    dob = models.DateField(validators=[validate_age])
    country = CountryField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["created_at"]
        db_table = "user_profile"

        indexes = [
            models.Index(fields=["contact_number"], name="contact_idx"),
            models.Index(fields=["email_id"], name="email_idx"),
        ]
