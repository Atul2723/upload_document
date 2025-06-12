from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.document_upload, name='document_upload'),
    path('upload-all/', views.checklist_upload_view, name='checklist_upload'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
]
