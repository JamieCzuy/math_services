# path("api/v2/file_import/", post_collections, name="file_import")
from django.urls import path
from .views import difference

urlpatterns = [
    path('difference/', difference),
]