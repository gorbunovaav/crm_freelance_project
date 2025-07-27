from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from .models import Lead
from client.models import Client
from team.models import Team


@login_required
def add_lead(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            team = Team.objects.filter(created_by=request.user)[0]
            lead.created_by = request.user
            lead.team = team
            lead.save()
            messages.info(request, "The lead was created")
            return redirect('leads:list')
    else:
        form = AddLeadForm()
    return render(request,'lead/add_lead.html', {
        'form': form,
        'team': team,
    })

@login_required
def delete_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()
    messages.info(request, "The lead was deleted")
    return redirect('leads:list')

@login_required
def edit_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.info(request, "The changes were saved")
            return redirect('leads:list')
    else:
        form = AddLeadForm(instance=lead)
    return render(request,'lead/edit_lead.html', {
        'form': form
    })
    
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)
    return render(request,'lead/leads_list.html', {
        'leads': leads
    })
    
@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    return render(request,'lead/lead_detail.html', {
        'lead': lead
    })
    
@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]
    client = Client.objects.create(
        name=lead.name,
        team=team,
        email=lead.email,
        phone=lead.phone,
        description=lead.description,
        created_by=request.user
        )
    lead.converted_to_client = True
    lead.save()
    messages.info(request, "The lead was converted to a client")
    return redirect('leads:list')
