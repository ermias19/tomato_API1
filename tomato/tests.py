from django.test import TestCase, Client
from rest_framework import status
from .models import Restourant ,Recipe , Ingredient
from .serializers import Restourant_Serializer ,Recipe_Serializer , Ingredient_Serializer

class RestourantViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.restaurant_data = {'resto_id':1, 'resto_name': 'Restaurant'}  # Adjust this data as needed
        self.restaurant = Restourant.objects.create(**self.restaurant_data)
        print("_________\t restaurant \t___________\n")

    def test_create_restaurant(self):
        response = self.client.post('/restorant', self.restaurant_data)
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        self.assertEqual(Restourant.objects.count(), 1)  
        print(":---> Viene aggiunta l'entità ristorante\n\n"  )

    def test_update_restaurant(self):
        self.assertIsNotNone(self.restaurant.resto_id)
        update_data = {'resto_id':1,'resto_name': 'Updated Restaurant'}
        serializer = Restourant_Serializer(instance=self.restaurant, data=update_data)
        
        
        if not serializer.is_valid():          
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())        
        response = self.client.patch(f'/restorant/{self.restaurant.resto_id}', serializer.data, content_type='application/json')            
        self.assertEqual(response.status_code, status.HTTP_200_OK)                
        self.restaurant.refresh_from_db() 
        print(":---> L'entità del ristorante è stata aggiornata\n\n")    

class RecipeViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        restaurant_data = {'resto_id': 1, 'resto_name': 'Restaurant'}        
        self.restaurant = Restourant.objects.create(**restaurant_data)
        
        self.recipe_data = {'Recipe_id':1, 'Recipename': 'pizza' ,'Restourant':self.restaurant}  
        self.recipe = Recipe.objects.create(**self.recipe_data)
        print("_________\t Recipe \t___________\n")
     

        

    def test_create_recipe(self):
        response = self.client.post('/recipes', self.recipe_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Recipe.objects.count(), 1)
        print(":---> L'entità ricetta viene creata\n")


    def test_update_recipe(self):
        self.assertIsNotNone(self.recipe.Recipe_id)

        restaurant_data = {'resto_id': 2, 'resto_name': 'Restaurant'}        
        self.restaurant = Restourant.objects.create(**restaurant_data)

        update_data = {'Recipe_id':1,'Recipename': 'pasta', 'Restourant':self.restaurant.resto_id}
        serializer = Recipe_Serializer(instance=self.recipe, data=update_data)
        
        if not serializer.is_valid():          
            print(serializer.errors)

        self.assertTrue(serializer.is_valid())        
        response = self.client.patch(f'/recipes/{self.recipe.Recipe_id}', serializer.data, content_type='application/json')            
        self.assertEqual(response.status_code, status.HTTP_200_OK)                
        self.recipe.refresh_from_db() 
        print(":---> Recipe entitry is updated\n\n")


class IngredientViewTests(TestCase):
    def setUp(self):
        self.client = Client()       
        self.ingredient_data = {'ing_id':1, 'Ingredientname': 'pizza'}  
        self.ingredient = Ingredient.objects.create(**self.ingredient_data)
        print("_________\t Ingredient \t___________\n")                                                       

    def test_create_ingredient(self):
        response = self.client.post('/ingredient', self.ingredient_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Ingredient.objects.count(), 1)
        print(":---> La voce ingrediente è stata creata correttamente\n\n")

    def test_update_ingredient(self):
        self.assertIsNotNone(self.ingredient.ing_id)                                                     
        update_data = {'ing_id':1,'Ingredientname': 'pasta' }
        serializer = Ingredient_Serializer(instance=self.ingredient, data=update_data)

        if not serializer.is_valid():          
            print(serializer.errors)
        
        self.assertTrue(serializer.is_valid())        
        response = self.client.patch(f'/ingredient/{self.ingredient.ing_id}', serializer.data, content_type='application/json')            
        self.assertEqual(response.status_code, status.HTTP_200_OK)                
        self.ingredient.refresh_from_db() 
        print(":--->La voce dell'ingrediente è stata aggiornata correttamente\n\n")


