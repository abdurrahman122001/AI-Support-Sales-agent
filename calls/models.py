from django.db import models

class CallerInfo(models.Model):
    call_id = models.CharField(max_length=100, unique=True)
    caller_number = models.CharField(max_length=50)

    MAIN_PATH_CHOICES = [
        ("sales", "Sales"),
        ("support", "Support"),
    ]
    main_path = models.CharField(
        max_length=20,
        choices=MAIN_PATH_CHOICES,
        help_text="“sales” or “support”"
    )

    CALLER_TYPE_CHOICES = [
        ("practitioner", "Practitioner"),
        ("client", "Client"),
    ]
    caller_type = models.CharField(
        max_length=20,
        choices=CALLER_TYPE_CHOICES,
        help_text="“practitioner” or “client”"
    )

    # Sales → Practitioner fields
    business_name = models.CharField(max_length=255, blank=True, null=True)
    practice_type = models.CharField(max_length=255, blank=True, null=True)
    primary_interest = models.CharField(max_length=500, blank=True, null=True)
    sales_email = models.EmailField(max_length=254, blank=True, null=True)

    # Sales → Client fields
    client_inquiry_focus = models.CharField(max_length=500, blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)

    # Support → Practitioner & Client fields
    account_identifier = models.CharField(max_length=255, blank=True, null=True)
    support_issue_summary = models.CharField(max_length=1000, blank=True, null=True)
    callback_number = models.CharField(max_length=50, blank=True, null=True)

    # Always capture the transcript
    transcript = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.call_id} – {self.caller_number} ({self.main_path}/{self.caller_type})"
