from rest_framework import generics
from rest_framework.response import Response 
from django.http import  JsonResponse
from rest_framework import status 
from ..models import  Recipe ,RecipeIngredient ,RecipeIngredient , Ingredient
from ..serializers import  Recipe_Serializer  ,RecipeIngredient_Serializer


class Recipe_view(generics.ListCreateAPIView):
    queryset=Recipe.objects.all()
    # print(queryset)
    serializer_class=Recipe_Serializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # print('yihe mndn nw',serializer.data)
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
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # print(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    # def get_queryset(self):
    #     Recipe_id=self.kwargs.get('Recipe_id')
    #     ingredient_id=self.kwargs.get('ingredient_id')
    #     print(Recipe_id)
    #     queryset=RecipeIngredient.objects.filter(recipe=Recipe_id  and Ingredient=ingredient_id)
    #     print(queryset)
    #     return queryset    
    
