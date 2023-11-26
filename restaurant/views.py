from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

# To generate AuthToken programmatically
# from rest_framework.authtoken.models import Token
# token = Token.objects.create(user="...")
# print(token.key)

# Authenticating users with @api_view
@api_view()
@permission_classes([IsAuthenticated])
def secure_view(request):
  return Response({"Message": "Granted with Authentication"})

# Authenticating users with ListCreateAPIView
class MenuItemsViewWithAuth(ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer




# Create your views here.
def index(request):
  return render(request, 'index.html', {})

# Using APIView
class BookingView(APIView):
  def get(self, request):
    items = Booking.objects.all()
    serializer = BookingSerializer(items, many= True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = BookingSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response({"status":"Success", "data": serializer.data})
  

class MenuView(APIView):
  def get(self, request):
    items = Menu.objects.all()
    serializer = MenuSerializer(items, many= True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = MenuSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response({"status":"Success", "data": serializer.data})
    

# Using generic views

class MenuItemView(ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer


# Using ModelViewSet
# With Authentication
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]