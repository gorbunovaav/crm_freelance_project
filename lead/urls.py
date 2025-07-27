from django.urls import path

from . import views

app_name='leads'

urlpatterns = [
    path("add-lead/", views.add_lead, name="add_lead"),
    path("<int:pk>/delete/", views.delete_lead, name="delete"),
    path("<int:pk>/edit/", views.edit_lead, name="edit"),
    path("<int:pk>/convert/", views.convert_to_client, name="convert"),
    path("", views.leads_list, name="list"),
    path("<int:pk>/", views.lead_detail, name="detail"),
]