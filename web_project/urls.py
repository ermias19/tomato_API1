from django.contrib import admin
from django.urls import path
from tomato import views
from tomato.tomato_views.recipe_view import Recipe_view , Recipe_detail_view ,recipt_ing_recipt 
from tomato.tomato_views.ingredient_view import Ingredient_view , Ingredient_detail_view ,ingred_resto_recipt

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('restorant/', views.Restourant_view.as_view(), name='restaurant'), 
    path('restorant/<int:pk>', views.Restorant_detail_view.as_view(), name='restaurant-detail'),
    path('restorant/<int:restaurant_id>/recipes', views.restorant_spec_recipt.as_view(), name='restaurant-recipe-detail'),

     path('recipes', Recipe_view.as_view(), name='recipe'), 
     path('recipes/<int:pk>', Recipe_detail_view.as_view(), name='restaurant-detail'),
     path('recipes/recipes_ingredient/<int:recipe_id>', recipt_ing_recipt.as_view(), name='recipe-ingredient-detail'),
     path('recipes/recipes_ingredient/', recipt_ing_recipt.as_view(), name='recipe-ingredient'),
    
    path('ingredient', Ingredient_view.as_view(), name='ingredient'), 
    path('ingredient/<int:pk>', Ingredient_detail_view.as_view(), name='restaurant-detail'),
    path('ingredient/ingredient_resturant/<int:ingred_id>', ingred_resto_recipt.as_view(), name='ingredient_restorantdetail'),
    path('ingredient/ingredient_resturant/', ingred_resto_recipt.as_view(), name='ingredient_restaurant_detail'),
    

]

"""
                        Django URLs Documentation

1. Admin URLs
Description: URLs related to the Django admin interface.

/admin/: The Django admin interface.
2. Restaurant URLs
Description: URLs related to restaurant views.

/restorant/: List view for restaurants.
/restorant/<int:pk>: Detail view for a specific restaurant.
/restorant/<int:restaurant_id>/recipes: List view for recipes associated with a specific restaurant.
3. Recipe URLs
Description: URLs related to recipe views.

/recipes/: List view for recipes.
/recipes/<int:pk>: Detail view for a specific recipe.
/recipes/recipes_ingredient/<int:recipe_id>: List view for ingredients associated with a specific recipe.
/recipes/recipes_ingredient/: List view for all recipe-ingredient relationships.
4. Ingredient URLs
Description: URLs related to ingredient views.

/ingredient/: List view for ingredients.
/ingredient/<int:pk>: Detail view for a specific ingredient.
/ingredient/ingredient_resturant/<int:ingred_id>: List view for restaurants associated with a specific ingredient.
/ingredient/ingredient_resturant/: List view for all ingredient-restaurant relationships.
Additional Notes:
View Classes:

The views associated with each URL pattern are specified using the as_view() method.
Name Parameter:

The name parameter in each URL pattern is used to create a unique identifier for the URL, which can be referenced in Django templates or when using the reverse() function.
Primary Key (<int:pk>):

The use of <int:pk> in some URL patterns indicates that the corresponding view expects an integer primary key as part of the URL."""