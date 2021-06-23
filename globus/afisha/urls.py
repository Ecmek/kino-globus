from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('show_end/', views.show_end, name='show_end'),
     path('add_cinema/', views.add_cinema, name='add_cinema'),
     path('add_show_time/', views.add_show_time, name='add_show_time'),
     path('<int:id_cinema>/edit/', views.edit_cinema, name='edit_cinema'),
     path('<int:id_cinema>/<int:id_session>/edit/', views.edit_session,
          name='edit_session'),
     path('<int:id_cinema>/<int:id_session>/confrim_delete/',
          views.confrim_delete_session, name='confrim_delete_session'),
     path('<int:id_cinema>/<int:id_session>/delete/', views.delete_session,
          name='delete_session'),
]
