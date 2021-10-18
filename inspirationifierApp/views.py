from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer
from .utils import process

# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def index(request):
    
    image = request.GET.get('image','')
    text = request.GET.get('text','')

    process(text, image)
    
    return HttpResponse("Hello")