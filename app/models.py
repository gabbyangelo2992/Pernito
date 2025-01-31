from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    DOCUMENT_TYPES = [
        ('Certificate of Residency', 'Certificate of Residency'),
        ('Barangay Clearance', 'Barangay Clearance'),
        ('Other', 'Other'),
    ]

    homeowner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"{self.document_type} Request by {self.homeowner.username}"
    def get_absolute_url(self):
        return reverse("list_request_document", kwargs={"pk": self.pk})

class Announcement(models.Model):
    subject = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="announcements")
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Announcement by {self.author}"

    def get_absolute_url(self):
        return reverse("detail_announcement", kwargs={"pk": self.pk})


class Property(models.Model):
    PROPERTY_TYPES = [
        ('House', 'House'),
        ('Condo', 'Condo'),
        ('Lot', 'Lot'),
    ]
    homeowner = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the logged-in user
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    size = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.homeowner.username} - {self.property_type} ({self.size} sqm)"

class Feedback(models.Model):
    subject = models.CharField(max_length=255,)
    homeowner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="feedback")
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date and time when feedback is created

    def __str__(self):
        return f"Feedback by {self.homeowner}"

    def get_absolute_url(self):
        return reverse("detail_feedback", kwargs={"pk": self.pk})






























