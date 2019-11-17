from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *

def index(request):
    if request.user.is_authenticated:
        return redirect('/scoreboard')
    else:
        return redirect('/login')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/scoreboard')
        else:
            return render(request, 'myScoreboard/login.html', {'bad_login': True})
    
    elif request.method == "GET":
        return render(request, 'myScoreboard/login.html', {'bad_login': False})

@login_required
def scoreboard(request):
    if request.method == "GET":
        teams = team.objects.all()
        return render(request, 'myScoreboard/scoreboard.html', {'teams': teams})

@login_required
def submit_flag(request):
    if request.method == "POST":
        userflag = request.POST['flagvalue']
        # Check flag against all flags in db
        flag_queries = flag.objects.filter(flag_value=userflag)
        flag_val = None
        if len(flag_queries) == 1:
            flag_val = flag_queries[0]

        if flag_val:
            
            points = flag_val.point_value
            player_team = team.objects.get(members=request.user)
            if flag_val in player_team.flags_gotten.all():
                return render(request, 'myScoreboard/submit_flag.html')
            else:
                player_team.flags_gotten.add(flag_val)
                
                player_team.team_points += points
                player_team.save()
                return redirect('/scoreboard')
        else:
            return render(request, 'myScoreboard/submit_flag.html')


    elif request.method == "GET":
        return render(request, 'myScoreboard/submit_flag.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/scoreboard')
    else:
        form = UserCreationForm()
    return render(request, 'myScoreboard/signup.html', {'form': form})

@login_required
def teamcreation(request):
    if request.method == "POST":
        user = request.user
        new_team_name = request.POST['teamname']
        if len(team.objects.filter(members=user)) == 0:
            queries = team.objects.filter(team_name=new_team_name)
            if len(queries) != 0:
                return render(request, 'myScoreboard/teamcreation.html')
            else:
                team.objects.create(team_name=new_team_name)
                #new_team.save()
                return redirect('/scoreboard')
        else:
            return redirect('/scoreboard')
    else:        
            return render(request, 'myScoreboard/teamcreation.html')

