from .models import ChessPiece
from rest_framework import serializers


class ChessPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessPiece
        fields = '__all__'