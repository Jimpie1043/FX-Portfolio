# documentation/views.py
from django.shortcuts import render

from .models import Document


def documentation(request):
    documents = Document.objects.prefetch_related("tags").all()
    return render(request, "documentation.html", {"documents": documents})