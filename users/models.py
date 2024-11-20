from django.db import models


class ComplianceMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    class Meta:
        verbose_name = "Compliance Form"
        verbose_name_plural = "Compliance Forms"
        permissions = [
            ("view_compliance_message", "Can view compliance forms"),
        ]


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"
        permissions = [
            ("view_contact_message", "Can view contact forms"),
        ]

class Referral(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    program_or_services = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='referrals/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Referral"
        verbose_name_plural = "Referrals"
        permissions = []  # Default permissions will be created automaticall

class Subscriber(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_view_subscribers", "Can view subscribers"),
        ]

    def __str__(self):
        return self.full_name