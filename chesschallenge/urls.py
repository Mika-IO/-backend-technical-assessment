from django.contrib import admin
from django.urls import path, include

from chesschallenge.chess import viewsets as chess_viewsets 
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'chess_pieces', chess_viewsets.ChessPiecesViewSet, basename='chess_pieces')
router.register(r'choice_options', chess_viewsets.ChessPiecesOptionsViewSet, basename='options')
router.register(r'knight_future_positions', chess_viewsets.KnightFuturePositions, basename='knight_future_positions')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
