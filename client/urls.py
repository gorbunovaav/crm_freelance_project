from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path("add/", views.add_client, name="add"),
    path("<int:pk>/edit/", views.edit_client, name="edit"),
    path("<int:pk>/delete/", views.delete_client, name="delete"),
    path("<int:pk>/add-comment/", views.client_detail, name="add_comment"),
    path("<int:pk>/add-file/", views.clients_add_file, name="add_file"),
    path("", views.clients_list, name="list"),
    path("<int:pk>/", views.client_detail, name="detail"),
    path("export/", views.clients_export, name="export"),
]