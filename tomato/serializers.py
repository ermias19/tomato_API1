from rest_framework import serializers
from .models import   Restourant , Recipe,Ingredient,RestaurantIngredient,RecipeIngredient

class Restourant_Serializer(serializers.ModelSerializer): 
        class Meta:
            model=Restourant
            fields=['resto_id','resto_name']
      

class Recipe_Serializer(serializers.ModelSerializer): 
        class Meta:
            model=Recipe
            fields=['Recipe_id','Recipename', 'Restourant']
            

class Ingredient_Serializer(serializers.ModelSerializer): 
        class Meta:
            model=Ingredient
            fields=['ing_id','Ingredientname']
                                

class RestaurantIngredient_Serializer(serializers.ModelSerializer): 
        class Meta:
            model=RestaurantIngredient
            fields=['Restourant','ingredient']
                        

class RecipeIngredient_Serializer(serializers.ModelSerializer): 
        class Meta:
              model=RecipeIngredient
              fields=['recipe','Ingredient','recipe_name','ingredient_name']
            
