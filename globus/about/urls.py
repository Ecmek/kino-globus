from django.urls import path

from . import views


app_name = 'about'

urlpatterns = [
    path('author/', views.AboutAuthorView.as_view(), name='author'),
    path('work_schedule/', views.AboutTechView.as_view(), name='work_schedule'),
]
