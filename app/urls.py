from django.urls import path
from .views import (HomePageView, AboutPageView, ContactPageView, FeedbackCreateView, FeedbackDeleteView,
                    FeedbackUpdateView, FeedbackListView, FeedbackDetailView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('feedback/', FeedbackListView.as_view(), name='list_feedback'),
    path('feedback/<int:pk>', FeedbackDetailView.as_view(), name='detail_feedback'),
    path('feedback/create', FeedbackCreateView.as_view(), name='create_feedback'),
    path('feedback/<int:pk>/edit', FeedbackUpdateView.as_view(), name='update_feedback'),
    path('feedback/<int:pk>/delete', FeedbackDeleteView.as_view(), name='delete_feedback'),




]



