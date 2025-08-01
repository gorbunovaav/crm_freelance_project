from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Userprofile
from .forms import SignupForm
from team.models import Team


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Team.objects.create(name='The team name', created_by=user)
            team.members.add(user)
            team.save()
            Userprofile.objects.create(user=user, active_team=team)
            return redirect('/log-in/')
    form = SignupForm()
    return render(request, 'userprofile/signup.html',{
        'form': form 
    })
    
@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')
    
