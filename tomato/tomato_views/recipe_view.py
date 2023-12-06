from rest_framework import generics
from rest_framework.response import Response 
from django.http import  JsonResponse
from rest_framework import status 
from ..models import  Recipe ,RecipeIngredient ,RecipeIngredient , Ingredient
from ..serializers import  Recipe_Serializer  ,RecipeIngredient_Serializer


class Recipe_view(generics.ListCreateAPIView):
    queryset=Recipe.objects.all()
  
    serializer_class=Recipe_Serializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
    
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class Recipe_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset=Recipe.objects.all()
    serializer_class=Recipe_Serializer    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class recipt_ing_recipt(generics.ListCreateAPIView):
    serializer_class = RecipeIngredient_Serializer
    queryset = RecipeIngredient.objects.all()

    def get(self, request, *args, **kwargs):
        recipe_id = self.kwargs.get('recipe_id')
            
        ermias = RecipeIngredient.objects.filter(recipe=recipe_id)
               
        data=[{  'recip_id':item.recipe.Recipe_id ,'recipe': item.recipe.Recipename, 'igredient_id':item.Ingredient.ing_id, 'ingredient': item.Ingredient.Ingredientname} for item in ermias]
        
        return JsonResponse(data, safe=False)
       

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
 
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
 
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    
"""Django Views Documentation
1. Recipe_view Class
    Description: Provides API endpoints for creating and listing recipes.

    Methods:
    GET: Lists all recipes.
    POST: Creates a new recipe.
    Request Parameters:
    GET: No parameters required.
    POST: Expects recipe data in the request body.
    Response:
    GET: Returns a list of serialized recipes.
    POST: Returns the serialized data of the created recipe.
2. Recipe_detail_view Class
    Description: Provides API endpoints for retrieving, updating, and deleting a specific recipe.

    Methods:
    GET: Retrieves details of a specific recipe.
    PUT / PATCH: Updates details of a specific recipe.
    DELETE: Deletes a specific recipe.
    Request Parameters:
    Expects the primary key (pk) of the recipe in the URL.
    Response:
    GET: Returns the serialized data of the requested recipe.
    PUT / PATCH: Returns the updated serialized data of the recipe.
    DELETE: Returns a success message.
3. recipt_ing_recipt Class
    Description: Provides API endpoints for creating and listing recipe-ingredient relationships based on a specific recipe.

    Methods:
    GET: Lists all recipe-ingredient relationships based on a specific recipe.
    POST: Creates a new recipe-ingredient relationship.
    Request Parameters:
    GET: Expects the recipe_id in the URL.
    POST: Expects recipe-ingredient relationship data in the request body.
    Response:
    GET: Returns a list of serialized recipe-ingredient relationships based on the specified recipe.
    POST: Returns the serialized data of the created recipe-ingredient relationship.
    Additional Notes:
    Serializer Classes:

    The views use serializer classes (Recipe_Serializer and RecipeIngredient_Serializer) to handle data serialization and deserialization.
    Error Handling:

    The views include error handling to validate incoming data and respond with appropriate status codes and error messages.
    HTTP Methods:

    The views utilize various HTTP methods (GET, POST, PUT, PATCH, DELETE) to perform different operations on the resources."""