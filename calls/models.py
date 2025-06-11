from django.db import models

class CallerInfo(models.Model):
    caller_number    = models.CharField(max_length=20)
    main_path        = models.CharField(max_length=20)
    caller_type      = models.CharField(max_length=20)
    business_name    = models.CharField(max_length=255)
    practice_type    = models.CharField(max_length=255)
    primary_interest = models.CharField(max_length=255)
    sales_email      = models.CharField(max_length=255)
    transcript       = models.TextField(blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.caller_number} @ {self.created_at:%Y-%m-%d %H:%M}"
