from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Feedback

class HomePageView(TemplateView):
    template_name = "app/home.html"

class AboutPageView(TemplateView):
    template_name = "app/about.html"

class ContactPageView(TemplateView):
    template_name = "app/contact.html"

class FeedbackListView(ListView):
    model = Feedback
    template_name = "app/list_feedback.html"

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = "app/detail_feedback.html"

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['subject', 'homeowner', 'feedback_text',]
    template_name = "app/create_feedback.html"

class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = "app/delete_feedback.html"
    success_url = reverse_lazy("list_feedback")

class FeedbackUpdateView(UpdateView):
    model = Feedback
    fields = ['subject', 'homeowner', 'feedback_text',]
    template_name = "app/update_feedback.html"
