from django.db import models
import uuid


class ChessPiece(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NAME_CHOICES = (
        ('King', 'King'),
        ('Rook', 'Rook'),
        ('Bishop', 'Bishop'),
        ('Queen', 'Queen'),
        ('Knight', 'Knight'),
        ('Pawn', 'Pawn'),
    )
    name = models.CharField('tipo', max_length=150, blank=False, choices=NAME_CHOICES)
    COLOR_CHOICES = (
        ('White', 'White'),
        ('Black', 'Black'),
    )
    color = models.CharField('cor', max_length=150, blank=False, choices=COLOR_CHOICES)