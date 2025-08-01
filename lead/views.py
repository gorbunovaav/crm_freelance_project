from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from .models import Lead
from .forms import AddCommentForm, AddFileForm
from client.models import Client, Comment as ClientComment
from team.models import Team
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class LeadListView(ListView, LoginRequiredMixin):
    model = Lead
    
    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, converted_to_client=False)
        

class LeadDetailView(DetailView, LoginRequiredMixin):
    model = Lead
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddCommentForm
        context["fileform"] = AddFileForm
        
        return context

    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))
    
class LeadDeleteView(DeleteView, LoginRequiredMixin):
    model = Lead
    success_url = reverse_lazy('leads:list')

    def get_queryset(self):
        queryset = super(LeadDeleteView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class LeadUpdateView(UpdateView, LoginRequiredMixin):
    model = Lead
    fields = ("name", "email", "phone", "description", 'priority', 'status')
    success_url = reverse_lazy('leads:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit lead'
        return context
    
    def get_queryset(self):
        queryset = super(LeadUpdateView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))
    
class LeadCreateView(CreateView, LoginRequiredMixin):
    model = Lead
    fields = ("name", "email", "phone", "description", 'priority', 'status')
    success_url = reverse_lazy('leads:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team"] = self.request.user.userprofile.active_team
        context["title"] = 'Add lead'
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = self.request.user.userprofile.active_team
        self.object.save()

        return super().form_valid(form)

class AddFileView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.team = self.request.user.userprofile.active_team
            file.created_by = request.user
            file.lead_id = pk
            file.save()
        return redirect('leads:detail', pk=pk)

class AddCommentView(View):    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.team = self.request.user.userprofile.active_team
            comment.created_by = request.user
            comment.lead_id = pk
            comment.save()
            
        return redirect('leads:detail', pk=pk)
            

class ConvertToClientView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        client = Client.objects.create(
            name=lead.name,
            team=self.request.user.userprofile.active_team,
            email=lead.email,
            phone=lead.phone,
            description=lead.description,
            created_by=request.user
        )
        lead.converted_to_client = True
        lead.save()
        comments = lead.comments.all()
        for comment in comments:
            ClientComment.objects.create(
                client = client,
                content = comment.content,
                created_by = comment.created_by,
                team = self.request.user.userprofile.active_team
            )
        messages.info(request, "The lead was converted to a client")
        return redirect('leads:list')

    
