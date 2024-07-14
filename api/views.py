from django.shortcuts import render

from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_to_api(request):
    return redirect('/api/items/')

def index(request):
    return HttpResponse("Welcome to the API")

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer