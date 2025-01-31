from django.urls import path, include
from .views import (HomePageView, AboutPageView, ContactPageView, FeedbackCreateView, FeedbackDeleteView,
                    FeedbackUpdateView, FeedbackListView,FeedbackmainListView, FeedbackDetailView,   )
from django.contrib.auth import views as auth_views
from . import views, admin
from .views import logout_view
from .views import balita_view
from .views import own_property

from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementDetailView,
    AnnouncementCreateView,
    AnnouncementDeleteView,
    AnnouncementUpdateView
)


urlpatterns = [
    path('request_document/', views.request_document, name='request_document'),
    path('documents/', views.list_request_document, name='list_request_document'),
    path('update/<int:pk>/', views.update_request_document, name='update_request_document'),
    path('delete/<int:pk>/', views.delete_request_document, name='delete_request_document'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('feedbackmain/', FeedbackmainListView.as_view(), name='list_feedbackmain'),
    path('feedback/', FeedbackListView.as_view(), name='list_feedback'),
    path('feedback/<int:pk>', FeedbackDetailView.as_view(), name='detail_feedback'),
    path('feedback/create', FeedbackCreateView.as_view(), name='create_feedback'),
    path('feedback/<int:pk>/edit', FeedbackUpdateView.as_view(), name='update_feedback'),
    path('feedback/<int:pk>/delete', FeedbackDeleteView.as_view(), name='delete_feedback'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.dashboard, name='profile'),
    path('own-property/', own_property, name='own_property'),
    path('own_property/', views.own_property, name='own_property'),
    path('request_document/', views.request_document, name='request_document'),
    path('logout/', logout_view, name='logout'),
    path('balita/', balita_view, name='balita'),
    path('register-property/', views.own_property, name='own_property'),
    path('announcement/', views.AnnouncementListView.as_view(), name='list_announcement'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='detail_announcement'),
    path('announcements/new/', AnnouncementCreateView.as_view(), name='create_announcement'),
    path('announcements/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='delete_announcement'),
    path('announcements/<int:pk>/edit', AnnouncementUpdateView.as_view(), name='update_announcement'),
]











