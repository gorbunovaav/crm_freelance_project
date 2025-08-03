from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from .models import Project
from .forms import AddProjectForm, AddFileForm, AddCommentForm
from client.models import Client, Comment as ClientComment
from userprofile.models import Userprofile
from team.models import Team
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class ProjectListView(ListView, LoginRequiredMixin):
    model = Project
    
    def get_queryset(self):
        user = self.request.user
        try:
            client = user.userprofile.client
        except Userprofile.DoesNotExist:
            # Пользователь без профиля — вернуть пустой queryset или как-то иначе обработать
            return Project.objects.none()
        return Project.objects.filter(client=client)
        

class ProjectDetailView(DetailView, LoginRequiredMixin):
    model = Project
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddProjectForm
    
        return context

    def get_queryset(self):
        queryset = super(ProjectDetailView, self).get_queryset()
        return queryset.filter(client__user=self.request.user, pk=self.kwargs.get('pk'))
    
class ProjectDeleteView(DeleteView, LoginRequiredMixin):
    model = Project
    success_url = reverse_lazy('projects:list')

    def get_queryset(self):
        queryset = super(ProjectDeleteView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ProjectUpdateView(UpdateView, LoginRequiredMixin):
    model = Project
    fields = ('name', 'description', 'budget', 'status', 'start date', 'end date')
    success_url = reverse_lazy('projects:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit project'
        return context
    
    def get_queryset(self):
        queryset = super(ProjectUpdateView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))
    
class ProjectCreateView(CreateView, LoginRequiredMixin):
    model = Project
    fields = ('name', 'description', 'budget', 'status', 'start_date', 'end_date')
    success_url = reverse_lazy('projects:list')
    
    def form_valid(self, form):
        # Получаем Client, связанный с текущим пользователем
        try:
            client = self.request.user.userprofile.client
        except Userprofile.DoesNotExist:
            form.add_error(None, "Userprofile does not exist.")
            return self.form_invalid(form)
        except Client.DoesNotExist:
            form.add_error(None, "Client does not exist.")
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
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.team = self.request.user.userprofile.active_team
            file.created_by = request.user
            file.project_id = pk
            file.save()
        return redirect('projects:detail', pk=pk)

class AddCommentView(View):    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.team = self.request.user.userprofile.active_team
            comment.created_by = request.user
            comment.project_id = pk
            comment.save()
            
        return redirect('projects:detail', pk=pk)
            

