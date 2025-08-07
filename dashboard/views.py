from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from lead.models import Lead
from client.models import Client
from client.models import Team

@login_required
def dashboard(request):
    team = Team.objects.filter(Q(created_by=request.user) | Q(members=request.user)).first()

    if not team:
        return render(request, 'dashboard/dashboard.html', {
            'leads': [],
            'clients': [],
            'error': 'Команда не найдена. Пожалуйста, создайте или присоединитесь к команде.'
        })

    # leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[:5]
    leads = Lead.objects.filter(converted_to_client=False).order_by('-created_at')[:5]

    clients = Client.objects.filter(team=team).order_by('-created_at')[:5]

    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })
    # team = Team.objects.filter(created_by=request.user)[0]
    # leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[0:5]
    # clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]

    # return render(request, 'dashboard/dashboard.html',{
    #     'leads':leads,
    #     'clients':clients,
    # })
