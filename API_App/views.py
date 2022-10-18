from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from API_App.models import *

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

import json, datetime, pytz
from django.core import serializers
from . import serializers as szs
import requests
import re

class DogList(APIView):
    """
    Present a list of all Dogs
    """

    def get(self, request, format=None):
        dog = Dog.objects.all()
        json_dogs = serializers.serialize('json', dog)
        return HttpResponse(json_dogs, content_type='json')

    def post(self, request, *args, **kwargs):
        newdog = Dog(
            name = request.data.get('name'),
            age = int(request.data.get('age')),
            breed = Breed.objects.get(pk=request.data.get('breed')),
            gender = request.data.get('gender'),
            color = request.data.get('color'),
            favoritefood = request.data.get('favoritefood'),
            favoritetoy = request.data.get('favoritetoy')
        )

        try:
            newdog.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        newdog.save()
        return Response({'success': True}, status=status.HTTP_200_OK)

class DogDetail(APIView):
    """
    Retreive details relating to a specific Dog
    """

    def get(self, request, id):
        dog = Dog.objects.get(pk=id)
        json_dog = serializers.serialize('json', [dog])
        return HttpResponse(json_dog, content_type='json')

    def put(self, request, id):
        try:
            dog = Dog.objects.get(pk=id)
            dog.name = request.data.get('name')
            dog.age = int(request.data.get('age'))
            dog.breed = Breed.objects.get(pk=request.data.get('breed'))
            dog.gender = request.data.get('gender')
            dog.color = request.data.get('color')
            dog.favoritefood = request.data.get('favoritefood')
            dog.favoritetoy = request.data.get('favoritetoy')
            dog.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        except BaseException as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        dog = Dog.objects.get(pk=id)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BreedList(APIView):
    """
    Present a list of all breeds
    """

    def get(self, request, format=None):
        breed = Breed.objects.all()
        json_breeds = serializers.serialize('json', breed)
        return HttpResponse(json_breeds, content_type='json')

    def post(self, request, *args, **kwargs):
        newbreed = Breed(
            name = request.data.get('name'),
            size = request.data.get('size'),
            friendliness = request.data.get('friendliness'),
            trainability = request.data.get('trainability'),
            sheddingamount = request.data.get('sheddingamount'),
            exersciseneeds = request.data.get('exersciseneeds')
        )

        try:
            newbreed.clean_fields()
        except ValidationError as e:
            print(e)
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        newbreed.save()
        return Response({'success': True}, status=status.HTTP_200_OK)


class BreedDetail(APIView):
    """
    Retreive details relating to a specific breed
    """
    def get(self, request, id):
        breed = Breed.objects.get(pk=id)
        json_breed = serializers.serialize('json', [breed])
        return HttpResponse(json_breed, content_type='json')

    def put(self, request, id):
        try:
            breed = Breed.objects.get(pk=id)
            breed.name = request.data.get('name')
            breed.size = request.data.get('size')
            breed.friendliness = request.data.get('friendliness')
            breed.trainability = request.data.get('trainability')
            breed.sheddingamount = request.data.get('sheddingamount')
            breed.exersciseneeds = request.data.get('exersciseneeds')
            breed.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        except BaseException as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        breed = Breed.objects.get(pk=id)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DogListViewSet(viewsets.ModelViewSet):
    """
    This endpoint serves to deliver dog data to the api
    """
    queryset = Dog.objects.all()
    serializer_class = szs.DogSerializer

class BreedListViewSet(viewsets.ModelViewSet):
    """
    This endpoint serves to deliver breed data to the api
    """
    queryset = Breed.objects.all()
    serializer_class = szs.BreedSerializer

@action(detail=True)
class DogDetailViewSet(viewsets.ModelViewSet):
    """
    This endpoint serves to deliver dog detail data to the api
    """
    queryset = Dog.objects.all()
    serializer_class = szs.DogSerializer

@action(detail=True)
class BreedDetailViewSet(viewsets.ModelViewSet):
    """
    This endpoint serves to deliver breed detail data to the api
    """
    queryset = Breed.objects.all()
    serializer_class = szs.BreedSerializer
