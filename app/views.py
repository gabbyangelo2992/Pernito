from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import PropertyForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib.auth.decorators import login_required
from .models import Feedback
from .forms import FeedbackForm  # Assuming you have a form for feedback
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Property
from .forms import DocumentForm
from .models import Document
from .forms import DocumentRequestForm  # Assuming you have a form class

@login_required

def request_document(request):
    if request.method == 'POST':
        document_type = request.POST.get('document_type')

        if document_type:
            # Assuming you have a model named 'Document'
            document = Document.objects.create(document_type=document_type, status="Pending")
            document.save()

            return redirect('list_request_document')  # Redirect to list view

    return render(request, 'app/request_document.html')


# List Document Requests view
@login_required
def list_request_document(request):
    documents = Document.objects.filter(homeowner=request.user)
    return render(request, 'app/list_request_document.html', {'documents': documents})


# Update Document Request view
@login_required
def update_request_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.document_type = request.POST.get('document_type')
        document.save()
        return redirect('list_request_document')

    return render(request, 'app/update_request_document.html', {'document': document})


# Delete Document Request view
@login_required
def delete_request_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('list_request_document')

    return render(request, 'app/delete_request_document.html', {'document': document})

@login_required
def own_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.owner = request.user  # Automatically set the logged-in user as the owner
            property_instance.save()
            return redirect('profile')  # Redirect to profile after submission
    else:
        form = PropertyForm()

    return render(request, 'own_property.html', {'form': form})


@login_required
def create_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.homeowner = request.user.homeowner  # Link to logged-in user's Homeowner object
            feedback.save()
            return redirect('list_feedback')  # Redirect to list of feedback after saving
    else:
        form = FeedbackForm()
    return render(request, 'create_feedback.html', {'form': form})


@login_required
def edit_feedback(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    if feedback.homeowner.user != request.user:
        return redirect('feedback_list')  # Prevent editing others' feedback

    if request.method == "POST":
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'edit_feedback.html', {'form': form})


@login_required
def delete_feedback(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    if feedback.homeowner.user != request.user:
        return redirect('feedback_list')  # Prevent deleting others' feedback

    feedback.delete()
    return redirect('feedback_list')

class AnnouncementListView(ListView):
    model = Announcement
    template_name = "app/list_announcement.html"
    context_object_name = "list_announcement"

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "app/detail_announcement.html"

class AnnouncementCreateView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "app/create_announcement.html"

class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = "app/delete_announcement.html"
    success_url = reverse_lazy("list_announcement")

class AnnouncementUpdateView(UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "app/update_announcement.html"



@login_required
def own_property(request):
    if request.method == "POST":
        property_type = request.POST.get("property_type")
        size = request.POST.get("size")

        if property_type and size:  # Ensure data is valid
            Property.objects.create(homeowner=request.user, property_type=property_type, size=size)
            return redirect("own_property")  # Redirect to clear the form

    properties = Property.objects.filter(homeowner=request.user)

    return render(request, "app/own_property.html", {"properties": properties})


class HomePageView(TemplateView):
    template_name = "app/home.html"

class AboutPageView(TemplateView):
    template_name = "app/about.html"

class ContactPageView(TemplateView):
    template_name = "app/contact.html"

class FeedbackListView(ListView):
    model = Feedback
    template_name = "app/list_feedback.html"

class FeedbackmainListView(LoginRequiredMixin,ListView):
    model = Feedback
    template_name = "app/list_feedbackmain.html"

class FeedbackDetailView(LoginRequiredMixin,DetailView):
    model = Feedback
    template_name = "app/detail_feedback.html"

class FeedbackCreateView(LoginRequiredMixin,CreateView):
    model = Feedback
    fields = ['subject',  'feedback_text',]
    template_name = "app/create_feedback.html"
    success_url = reverse_lazy("list_feedback")  # Adjust as needed

    def form_valid(self, form):
        form.instance.homeowner = self.request.user  # Link feedback to logged-in user
        return super().form_valid(form)


class FeedbackDeleteView(LoginRequiredMixin, DeleteView):
    model = Feedback
    template_name = "app/delete_feedback.html"
    success_url = reverse_lazy("list_feedback")

class FeedbackUpdateView(LoginRequiredMixin,UpdateView):
    model = Feedback
    fields = ['subject', 'homeowner', 'feedback_text',]
    template_name = "app/update_feedback.html"
    success_url = '/profile/'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves the user to the database
            login(request, user)  # Logs in the user automatically
            messages.success(request, "Registration successful!")  # Flash message
            return redirect('login')  # Redirect after successful registration
        else:
            messages.error(request, "There was an error with your registration.")  # Flash error message
    else:
        form = UserCreationForm()  # Instantiate the empty form for GET requests

    return render(request, 'app/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'app/profile.html')

@login_required
def own_property(request):
    return render(request, 'app/own_property.html')

@login_required
def request_document(request):
    return render(request, 'app/request_document.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Make sure 'login' is the correct URL name for your login page

def balita_view(request):
    return render(request, 'app/balita.html')

def dashboard(request):
    document_list = Document.objects.filter(homeowner=request.user)  # Getting feedback from the logged-in user
    return render(request, 'app/profile.html', {'list_document': document_list})

def dashboard(request):
    feedback_list = Feedback.objects.filter(homeowner=request.user)  # Getting feedback from the logged-in user
    return render(request, 'app/profile.html', {'list_feedback': feedback_list})