from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('games/', views.games, name='games'),
    path('addGame/', views.addGame, name='add'),
    path('updateGame/<int:id>', views.updateGame, name='update'),
    path('deleteGame/<int:id>', views.deleteGame, name='delete'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
