from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('games/', views.games, name='games'),
    path('addGame/', views.addGame, name='add'),
    path('updateGame/', views.updateGame, name='update'),
    path('deleteGame/', views.deleteGame, name='delete'),
    path('contact/', views.contact, name='contact')
]
