from django.db import models

class Restourant(models.Model):

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
      


"""1. Restourant Model
      Description: Represents a restaurant.

      Fields:

      resto_id: IntegerField (Primary Key)
      Description: Unique identifier for the restaurant.
      resto_name: CharField
      Description: The name of the restaurant.
      Methods:

      __str__(self): Returns the name of the restaurant as a string.
2. Recipe Model
      Description: Represents a recipe associated with a restaurant.

      Fields:

      Recipe_id: IntegerField (Primary Key)
      Description: Unique identifier for the recipe.
      Recipename: CharField
      Description: The name of the recipe.
      Restourant: ForeignKey to Restourant model (on_delete=models.CASCADE)
      Description: Relationship with the Restourant model, indicating the restaurant associated with the recipe.
3. Ingredient Model
      Description: Represents an ingredient.

      Fields:

      ing_id: IntegerField (Primary Key)
      Description: Unique identifier for the ingredient.
      Ingredientname: CharField
      Description: The name of the ingredient.
4. RestaurantIngredient Model
      Description: Represents a relationship between a restaurant and an ingredient.

      Fields:

      Restourant: ForeignKey to Restourant model (on_delete=models.CASCADE)
      Description: Relationship with the Restourant model, indicating the associated restaurant.
      ingredient: ForeignKey to Ingredient model (on_delete=models.CASCADE)
      Description: Relationship with the Ingredient model, indicating the associated ingredient.
      Properties:

      recipe_name: Returns the name of the restaurant using the Restourant relationship.
      ingredient_name: Returns the name of the ingredient using the ingredient relationship.
5. RecipeIngredient Model
      Description: Represents a relationship between a recipe and an ingredient.

      Fields:

      recipe: ForeignKey to Recipe model (on_delete=models.CASCADE)
      Description: Relationship with the Recipe model, indicating the associated recipe.
      Ingredient: ForeignKey to Ingredient model (on_delete=models.CASCADE)
      Description: Relationship with the Ingredient model, indicating the associated ingredient.
      Properties:

      recipe_name: Returns the name of the recipe using the recipe relationship.
      ingredient_name: Returns the name of the ingredient using the Ingredient relationship."""      