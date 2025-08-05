from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from .models import Project
from .forms import AddProjectForm, AddFileForm
from client.models import Client, Comment as ClientComment
from userprofile.models import Userprofile
from team.models import Team
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class ProjectListView(ListView, LoginRequiredMixin):
    model = Project
    
    def get_queryset(self):
        queryset = super(ProjectListView, self).get_queryset()
        return queryset.filter(client__created_by=self.request.user)
        

class ProjectDetailView(DetailView, LoginRequiredMixin):
    model = Project
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddProjectForm
        context["fileform"] = AddFileForm()
    
        return context

    def get_queryset(self):
        queryset = super(ProjectDetailView, self).get_queryset()
        return queryset.filter(client__created_by=self.request.user, pk=self.kwargs.get('pk'))
    
class ProjectDeleteView(DeleteView, LoginRequiredMixin):
    model = Project
    success_url = reverse_lazy('projects:list')

    def get_queryset(self):
        queryset = super(ProjectDeleteView, self).get_queryset()
        return queryset.filter(client__created_by=self.request.user, pk=self.kwargs.get('pk'))
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ProjectUpdateView(UpdateView, LoginRequiredMixin):
    model = Project
    form_class = AddProjectForm
    success_url = reverse_lazy('projects:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit project'
        return context
    
    def get_queryset(self):
        queryset = super(ProjectUpdateView, self).get_queryset()
        return queryset.filter(client__created_by=self.request.user, pk=self.kwargs.get('pk'))
    
class ProjectCreateView(CreateView, LoginRequiredMixin):
    model = Project
    form_class = AddProjectForm
    success_url = reverse_lazy('projects:list')
    
    def form_valid(self, form):
        try:
            client = Client.objects.filter(created_by=self.request.user).first()
        except Client.DoesNotExist:
            form.add_error(None, "Client does not exist for this user.")
            return self.form_invalid(form)

        form.instance.client = client
        form.instance.team = self.request.user.userprofile.active_team
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team"] = self.request.user.userprofile.active_team
        context["title"] = 'Add project'
        return context

class AddFileView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        fileform = AddFileForm(request.POST, request.FILES)
        if fileform.is_valid():
            file = fileform.save(commit=False)
            file.team = self.request.user.userprofile.active_team
            file.created_by = request.user
            file.project_id = pk
            file.save()
        return redirect('projects:detail', pk=pk)

