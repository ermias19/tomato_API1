from django.db import models

class Restourant(models.Model):
      # resto_id = models.IntegerField() 
      resto_id=models.IntegerField(primary_key=True)
      resto_name=models.CharField(max_length=255)

      def __str__(self):
        return self.resto_name
 

class Recipe(models.Model):
      Recipe_id=models.IntegerField(primary_key=True)
      Recipename=models.CharField(max_length=255)
      Restourant=models.ForeignKey(Restourant, on_delete=models.CASCADE)      

class Ingredient(models.Model):
      ing_id=models.IntegerField(primary_key=True)
      Ingredientname=models.CharField(max_length=255)

class RestaurantIngredient(models.Model):
      Restourant=models.ForeignKey(Restourant, on_delete=models.CASCADE)
      ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE)

      @property
      def recipe_name(self):
        return self.Restourant.resto_name

      @property
      def ingredient_name(self):
            return self.ingredient.ingredient_name

class RecipeIngredient(models.Model):
      recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
      Ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE)
      
      @property
      def recipe_name(self):
        return self.recipe.recipe_name

      @property
      def ingredient_name(self):
            return self.ingredient.ingredient_name