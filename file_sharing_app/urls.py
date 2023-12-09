from django.urls import path
from .views import dashboard, upload_file, search_users, share_file


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('upload/', upload_file, name='upload_file'),
    path('search/', search_users, name='search_users'),
    path('share/<int:file_id>/', share_file, name='share_file')
]
