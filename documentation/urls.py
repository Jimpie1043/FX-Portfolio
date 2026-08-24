from django.urls import path
from . import views

app_name = "documentation"

urlpatterns = [
    path("documentation/", views.documentation, name='documentation'),
]