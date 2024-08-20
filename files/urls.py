from django.urls import path
from files.views import FileUploadView, FileDetailView, FileListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('files/upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/<uuid:file_id>/', FileDetailView.as_view(), name='file-detail'),
    path('files/', FileListView.as_view(), name='file-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)