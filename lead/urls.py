from django.urls import path

from . import views

urlpatterns = [
    path("add-lead/", views.add_lead, name="add_lead"),
    path("", views.leads_list, name="leads_list"),
    path("<int:pk>/", views.lead_detail, name="lead_detail"),
]