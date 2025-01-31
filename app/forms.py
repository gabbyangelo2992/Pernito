from django import forms
from .models import Property
from .models import Announcement
from .models import Feedback
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_type']

class DocumentRequestForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_type']

class DocumentRequest(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_type']




class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_type', 'size']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['subject', 'author', 'content']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'homeowner', 'feedback_text', ]