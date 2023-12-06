from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status 
from ..models import  Ingredient ,RestaurantIngredient
from ..serializers import  Ingredient_Serializer  , RestaurantIngredient_Serializer
from django.http import  JsonResponse


class Ingredient_view(generics.ListCreateAPIView):
    queryset=Ingredient.objects.all()

    serializer_class=Ingredient_Serializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class Ingredient_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ingredient.objects.all()
    serializer_class=Ingredient_Serializer    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class ingred_resto_recipt(generics.ListCreateAPIView):
    serializer_class = RestaurantIngredient_Serializer
    queryset = RestaurantIngredient.objects.all()
   

    def get(self, request, *args, **kwargs):
        ingred_id = self.kwargs.get('ingred_id')
       
            
        ermias = RestaurantIngredient.objects.filter(ingredient=ingred_id)
       
               
        data=[{  'ing_id':item.ingredient.ing_id ,'Ingredientname': item.ingredient.Ingredientname, 'resto_id':item.Restourant.resto_id, 'resto_name': item.Restourant.resto_name} for item in ermias]
        
        return JsonResponse(data, safe=False)
       

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


"""
Django Views Documentation
1. Ingredient_view Class
    Description: Provides API endpoints for creating and listing ingredients.

    Methods:
    GET: Lists all ingredients.
    POST: Creates a new ingredient.
    Request Parameters:
    GET: No parameters required.
    POST: Expects ingredient data in the request body.
    Response:
    GET: Returns a list of serialized ingredients.
    POST: Returns the serialized data of the created ingredient.
2. Ingredient_detail_view Class
    Description: Provides API endpoints for retrieving, updating, and deleting a specific ingredient.

    Methods:
    GET: Retrieves details of a specific ingredient.
    PUT / PATCH: Updates details of a specific ingredient.
    DELETE: Deletes a specific ingredient.
    Request Parameters:
    Expects the primary key (pk) of the ingredient in the URL.
    Response:
    GET: Returns the serialized data of the requested ingredient.
    PUT / PATCH: Returns the updated serialized data of the ingredient.
    DELETE: Returns a success message.
3. ingred_resto_recipt Class
    Description: Provides API endpoints for creating and listing restaurant-ingredient relationships based on a specific ingredient.

    Methods:
    GET: Lists all restaurant-ingredient relationships based on a specific ingredient.
    POST: Creates a new restaurant-ingredient relationship.
    Request Parameters:
    GET: Expects the ingred_id in the URL.
    POST: Expects restaurant-ingredient relationship data in the request body.
    Response:
    GET: Returns a list of serialized restaurant-ingredient relationships based on the specified ingredient.
    POST: Returns the serialized data of the created restaurant-ingredient relationship.
    Additional Notes:
    Serializer Classes:

    The views use serializer classes (Ingredient_Serializer and RestaurantIngredient_Serializer) to handle data serialization and deserialization.
    Error Handling:

    The views include error handling to validate incoming data and respond with appropriate status codes and error messages.
    HTTP Methods:

    The views utilize various HTTP methods (GET, POST, PUT, PATCH, DELETE) to perform different operations on the resources.
"""