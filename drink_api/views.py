# from django.shortcuts import render
# from django.http import JsonResponse


from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drink_api.permissions import IsAdmin
from .serializers import DrinkSerializer

from drink_api.models import Drink


class DrinkListCreate(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)

        return Response(serializer.data)

    def post(self, request):
        pass
    pass

