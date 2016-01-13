from rest_framework import viewsets
from rest_framework import status
from django.core.exceptions import  ObjectDoesNotExist

from .models import Card, CardType
from .serializers import CardSerializer, CardTypeSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @list_route()
    def count(self, request):
        return Response(Card.objects.count())

    @detail_route()
    def modified(self, request, pk):
        try:
            card = Card.objects.get(pk=pk)
            return Response(card.modified)
        except ObjectDoesNotExist:
            return Response('Card not Exist', status=status.HTTP_400_BAD_REQUEST)


class CardTypeViewSet(viewsets.ModelViewSet):
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerializer

