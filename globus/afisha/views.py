from django.shortcuts import render

from .models import Cinema


def index(request):
    films = Cinema.objects.all()
    return render(request, index.html, {'films': films})
