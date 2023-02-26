from storage import views
from django.urls import path


urlpatterns = [
    path("storage/", views.StorageView.as_view()),
]
