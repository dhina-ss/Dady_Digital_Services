from django.db import models

class SubscribeUser(models.Model):
    user_mail = models.EmailField(max_length=50, unique=True)  # Unique constraint if needed
    subscribed_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_mail


class ContactUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_mail = models.EmailField(max_length=50)
    user_number = models.CharField(max_length=15)  # Allow longer numbers for international formats
    user_message = models.TextField(null=True, blank=True)  # Nullable and blankable field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
