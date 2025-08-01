from django.urls import path

from . import views

app_name = 'team'

urlpatterns = [
    path("<int:pk>/edit/", views.edit_team, name="edit"),
    path("<int:pk>/detail/", views.detail_team, name="detail"),
    path("<int:pk>/activate/", views.activate_team, name="activate"),
    path("", views.teams_list, name="list"),

]