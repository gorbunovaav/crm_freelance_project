from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import index,about
from userprofile.forms import LoginForm

from django.contrib.auth import views

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("log-in/", views.LoginView.as_view(template_name="userprofile/login.html", authentication_form=LoginForm), name="login"),
    path("log-out/", views.LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("dashboard/", include('dashboard.urls')),
    path("dashboard/", include('userprofile.urls')),
    path("dashboard/leads/", include('lead.urls')),
    path("dashboard/clients/", include('client.urls')),
    path("dashboard/teams/", include('team.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
