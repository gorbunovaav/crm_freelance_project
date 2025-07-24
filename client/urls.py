from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.add_client, name="add_client"),
    path("<int:pk>/edit/", views.edit_client, name="edit_client"),
    path("<int:pk>/delete/", views.delete_client, name="delete_client"),
    path("", views.clients_list, name="clients_list"),
    path("<int:pk>/", views.client_detail, name="client_detail"),
]