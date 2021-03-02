from django.db import models


class MSOrderVouchers(models.Model):
    voucher_no = models.CharField(
        primary_key=True, blank=False, max_length=255, null=False
    )
    pin = models.CharField(blank=False, max_length=255)
    amount = models.IntegerField(blank=False)

    class Meta:
        app_label = "api"
