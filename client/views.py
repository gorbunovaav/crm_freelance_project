from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Client
from team.models import Team
from .forms import AddClientForm, AddCommentForm

@login_required
def add_client(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            team = Team.objects.filter(created_by=request.user)[0]
            client.created_by = request.user
            client.team = team
            client.save()
            messages.info(request, "The client was created")
            return redirect('clients:list')
    else:
        form = AddClientForm()
    return render(request,'client/add_client.html', {
        'form': form,
        'team': team,
    })
    
@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request,'client/clients_list.html', {
        'clients': clients
    })
    
@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            comment.client = client
            comment.save()
            return redirect('clients:detail', pk=pk)
    else:
        form = AddCommentForm()
            
    return render(request,'client/client_detail.html', {
        'client': client,
        'form': form
    })
    
@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()
    messages.info(request, "The client was deleted")
    return redirect('clients:list')

@login_required
def edit_client(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.info(request, "The changes were saved")
            return redirect('clients:list')
    else:
        form = AddClientForm(instance=client)
    return render(request,'client/edit_client.html', {
        'form': form 
    })
    

