from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Feedback(models.Model):
    subject = models.CharField(max_length=255,)
    homeowner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="feedback")
    feedback_text = models.TextField()
    date_submitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.homeowner}"

    def get_absolute_url(self):
        return reverse("detail_feedback", kwargs={"pk": self.pk})

































