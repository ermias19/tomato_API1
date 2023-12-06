from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from .models import Restourant , Recipe, Ingredient, RestaurantIngredient, RecipeIngredient
from .serializers import Restourant_Serializer , Recipe_Serializer ,  Ingredient_Serializer , RestaurantIngredient_Serializer , RecipeIngredient_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

class Restourant_view(generics.ListCreateAPIView):
    queryset=Restourant.objects.all()
   
    serializer_class=Restourant_Serializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
       
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Restorant_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset=Restourant.objects.all()
    serializer_class=Restourant_Serializer    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
class restorant_spec_recipt(generics.ListAPIView):
    serializer_class=Recipe_Serializer
    def get_queryset(self,*args, **kwargs ):
        restaurant_id=self.kwargs.get('restaurant_id')
     
        queryset=Recipe.objects.filter(Restourant=restaurant_id)
        return queryset
    

"""             Django Views Documentation

1. Restourant_view Class
    Description: Provides API endpoints for creating and listing restaurants.

    Methods:
    GET: Lists all restaurants.
    POST: Creates a new restaurant.
    Request Parameters:
    GET: No parameters required.
    POST: Expects restaurant data in the request body.
    Response:
    GET: Returns a list of serialized restaurants.
    POST: Returns the serialized data of the created restaurant.
2. Restorant_detail_view Class
    Description: Provides API endpoints for retrieving, updating, and deleting a specific restaurant.

    Methods:
    GET: Retrieves details of a specific restaurant.
    PUT / PATCH: Updates details of a specific restaurant.
    DELETE: Deletes a specific restaurant.
    Request Parameters:
    Expects the primary key (pk) of the restaurant in the URL.
    Response:
    GET: Returns the serialized data of the requested restaurant.
    PUT / PATCH: Returns the updated serialized data of the restaurant.
    DELETE: Returns a success message.
3. restorant_spec_recipt Class
        Description: Provides API endpoint for listing recipes associated with a specific restaurant.

        Methods:
        GET: Lists all recipes associated with a specific restaurant.
        Request Parameters:
        Expects the restaurant_id in the URL.
        Response:
        Returns a list of serialized recipes associated with the specified restaurant.
        Additional Notes:
        Serializer Classes:

        The views use serializer classes (Restourant_Serializer and Recipe_Serializer) to handle data serialization and deserialization.
    Error Handling:

    The views include error handling to validate incoming data and respond with appropriate status codes and error messages.
    HTTP Methods:

    The views utilize various HTTP methods (GET, POST, PUT, PATCH, DELETE) to perform different operations on the resources."""




