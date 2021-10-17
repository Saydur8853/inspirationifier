from django.shortcuts import render
from .models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer

# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def index(request):
    image = Image.objects.all().first()

    con = {
        'image': image,
    }

    return render(request,con)