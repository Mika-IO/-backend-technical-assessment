from .models import ChessPiece
from .serializers import ChessPieceSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response

class ChessPiecesViewSet(viewsets.ModelViewSet):
    """
    View to register chess pieces on API
    """
    queryset = ChessPiece.objects.all()
    serializer_class = ChessPieceSerializer


class ChessPiecesOptionsViewSet(viewsets.ViewSet):
    """
    View to GET list of name and color options
    """
    def list(self, request):
        options = {
            "name_options": [
                "King",
                "Rook",
                "Bishop",
                "Queen",
                "Knight",
                "Pawn"
            ],
            "color_options": [
                "Black",
                "White"
            ]
        }
        return Response(options)


class KnightFuturePositions(viewsets.ViewSet):
    """
    GET http://api/knight_future_positions/ 
    
        to see all Knights in the system
    
    
    GET http://api/knight_future_positions/id?coordinate=current_coordinate 
        
        to see future Knight positions in 2 turns
        
        * id -> ID of Knight
        * coordinate -> current coordinate of chess piece with following format a1 (Algebraic notation)
    """
    def list(self, request):
        queryset = ChessPiece.objects.filter(name="Knight")
        if queryset:
            chess_piece = get_object_or_404(queryset)
            serializer = ChessPieceSerializer(chess_piece)
            return Response(serializer.data)
        else:
            return Response({"message": "No Knight in database"})
    
    def retrieve(self, request, pk=None):
        coordinate = request.query_params.get('coordinate')
        if not coordinate:
            return Response({"message": "set a coordinate"})

        chess_piece = ChessPiece.objects.get(id=pk, name="Knight")
        if chess_piece:
            first_turn = [1, 2, 3, 4, 5]
            second_turn = [1, 2, 3, 4, 5]
            data = {
                "id": chess_piece.id,
                "name": chess_piece.name,
                "color": chess_piece.color,
                "future_coordinates_in_first_turn": first_turn,
                "future_coordinates_in_second_turn": second_turn,
            }

        else:
            return Response(
                {
                    "message": "id is not valid or does not exist"
                }
            )
        return Response(data)