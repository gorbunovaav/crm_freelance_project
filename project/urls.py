from django.urls import path

from . import views

app_name='projects'

urlpatterns = [
    path("add-project/", views.ProjectCreateView.as_view(), name="add"),
    path("<int:pk>/delete/", views.ProjectDeleteView.as_view(), name="delete"),
    path("<int:pk>/edit/", views.ProjectUpdateView.as_view(), name="edit"),
    path("<int:pk>/add-file/",views.AddFileView.as_view(), name="add_file"),
    path("<int:pk>/add-comment/",views.AddCommentView.as_view(), name="add_comment"),
    path("", views.ProjectListView.as_view(), name="list"),
    path("<int:pk>/", views.ProjectDetailView.as_view(), name="detail"),
]