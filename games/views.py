from django.shortcuts import render, HttpResponse
from .models import Game

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
    return render(request, 'addgame.html')

def updateGame(request):
    return render(request, 'updategame.html')

def deleteGame(request):
    return HttpResponse('DELETE GAME')

def contact(request):
    return render(request, 'contact.html')