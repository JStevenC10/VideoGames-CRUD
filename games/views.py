from django.shortcuts import render, redirect, HttpResponse
from .models import Game
from .forms import GameForm

# Create your views here.

def blog(request):
    return render(request, 'blog.html')

def games(request):
    allGames = Game.objects.all()
    context = {
        'games' : allGames
    }
    return render(request, 'games.html', context)

def addGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(to=games)
        return render(request, 'addgame.html', {'form' : form})
    else:
        form = GameForm()
        return render(request, 'addgame.html', {'form' : form})

def updateGame(request, id):
    updGame = Game.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        plataforms = request.POST['plataforms']
        category = request.POST['category']
        image = request.FILES['image']
        updGame.name = name
        updGame.plataforms = plataforms
        updGame.category = category
        updGame.image = image
        updGame.save()
        return redirect(to=games)
    else:
        return render(request, 'updategame.html', {'game' : updGame})


def deleteGame(request, id):
    delGame = Game.objects.get(id=id)
    delGame.delete()
    return redirect(to=games)

def contact(request):
    return render(request, 'contact.html')