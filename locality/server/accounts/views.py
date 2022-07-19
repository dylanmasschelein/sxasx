from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from accounts.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from accounts.models import User, Customer, ServiceProvider, Business
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


# # Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomerRegisterView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer.CustomerSerializer


class ServiceProviderRegisterView(generics.CreateAPIView):
    queryset = ServiceProvider.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer.ServiceProviderSerializer


class BusinessSerializer(generics.CreateAPIView):
    queryset = Business.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer.BusinessSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/account/token/',
        '/account/register/',
        '/account/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)