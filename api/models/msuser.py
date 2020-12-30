from django.db import models
from api.constants import USER_CURRENT_STATUS_CHOICES, ACTIVE


class MSUser(models.Model):
    tag_no = models.CharField(primary_key=True, max_length=255, editable=False)
    password = models.CharField(blank=True, null=True, max_length=255)
    phone_number = models.CharField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False, db_index=True)
    flipkart_email = models.EmailField(
        max_length=255, blank=True, null=True, unique=True, db_index=True
    )
    amazon_email = models.EmailField(
        max_length=255, blank=True, null=True, unique=True, db_index=True
    )
    is_authy_verified = models.BooleanField(default=False)
    current_status = models.CharField(
        blank=False, default=ACTIVE, max_length=255, choices=USER_CURRENT_STATUS_CHOICES
    )

    class Meta:
        app_label = "api"
