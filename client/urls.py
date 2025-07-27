from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path("add/", views.add_client, name="add"),
    path("<int:pk>/edit/", views.edit_client, name="edit"),
    path("<int:pk>/delete/", views.delete_client, name="delete"),
    path("", views.clients_list, name="list"),
    path("<int:pk>/", views.client_detail, name="detail"),
]