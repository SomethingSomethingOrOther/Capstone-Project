from django.shortcuts import render
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
        queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
        queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
       queryset = Booking.objects.all()
       serializer_class = BookingSerializer
       permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

