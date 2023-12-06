# tomato_API1
Tomato API Documentation
Welcome to the documentation for the Tomato API! This guide provides an overview of the Django-based Tomato API and its essential components.

Models
1. Restourant Model
Fields:
resto_id: IntegerField (Primary Key)
resto_name: CharField
2. Recipe Model
Fields:
Recipe_id: IntegerField (Primary Key)
Recipename: CharField
Restourant: ForeignKey to Restourant model (on_delete=models.CASCADE)
3. Ingredient Model
Fields:
ing_id: IntegerField (Primary Key)
Ingredientname: CharField
4. RestaurantIngredient Model
Fields:
Restourant: ForeignKey to Restourant model (on_delete=models.CASCADE)
ingredient: ForeignKey to Ingredient model (on_delete=models.CASCADE)
5. RecipeIngredient Model
Fields:
recipe: ForeignKey to Recipe model (on_delete=models.CASCADE)
Ingredient: ForeignKey to Ingredient model (on_delete=models.CASCADE)
Views
1. Restourant_view
Description: Provides API endpoints for creating and listing restaurants.
Methods:
GET: Lists all restaurants.
POST: Creates a new restaurant.
2. Restorant_detail_view
Description: Provides API endpoints for retrieving, updating, and deleting a specific restaurant.
Methods:
GET: Retrieves details of a specific restaurant.
PUT / PATCH: Updates details of a specific restaurant.
DELETE: Deletes a specific restaurant.
3. restorant_spec_recipt
Description: Provides API endpoint for listing recipes associated with a specific restaurant.
Methods:
GET: Lists all recipes associated with a specific restaurant.
4. Ingredient_view
Description: Provides API endpoints for creating and listing ingredients.
Methods:
GET: Lists all ingredients.
POST: Creates a new ingredient.
5. Ingredient_detail_view
Description: Provides API endpoints for retrieving, updating, and deleting a specific ingredient.
Methods:
GET: Retrieves details of a specific ingredient.
PUT / PATCH: Updates details of a specific ingredient.
DELETE: Deletes a specific ingredient.
6. ingred_resto_recipt
Description: Provides API endpoints for creating and listing restaurant-ingredient relationships based on a specific ingredient.
Methods:
GET: Lists all restaurant-ingredient relationships based on a specific ingredient.
POST: Creates a new restaurant-ingredient relationship.
7. Recipe_view
Description: Provides API endpoints for creating and listing recipes.
Methods:
GET: Lists all recipes.
POST: Creates a new recipe.
8. Recipe_detail_view
Description: Provides API endpoints for retrieving, updating, and deleting a specific recipe.
Methods:
GET: Retrieves details of a specific recipe.
PUT / PATCH: Updates details of a specific recipe.
DELETE: Deletes a specific recipe.
9. recipt_ing_recipt
Description: Provides API endpoints for creating and listing recipe-ingredient relationships based on a specific recipe.
Methods:
GET: Lists all recipe-ingredient relationships based on a specific recipe.
POST: Creates a new recipe-ingredient relationship.
Dockerfile
Base Image:
Uses Python 3.10 as the base image for the Docker container.
Environment Configuration:
Sets unbuffered mode for Python.
Working Directory:
Sets the working directory to /code/.
Copy Requirements:
Copies the requirements.txt file to the container.
Install Dependencies:
Installs Python dependencies specified in requirements.txt.
Copy Code:
Copies all files from the local directory to the /code/ directory inside the container.
Run Migrations:
Applies Django database migrations.
Expose Port:
Informs Docker that the application uses port 8000.
Default Command:
Sets the default command to run the Django development server.
