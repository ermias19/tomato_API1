"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tomato import views
from tomato.tomato_views.recipe_view import Recipe_view , Recipe_detail_view ,recipt_ing_recipt 
from tomato.tomato_views.ingredient_view import Ingredient_view , Ingredient_detail_view ,ingred_resto_recipt

urlpatterns = [
    path('admin/', admin.site.urls),
    # resturant starts here
    path('restorant/', views.Restourant_view.as_view(), name='restaurant'), 
    path('restorant/<int:pk>', views.Restorant_detail_view.as_view(), name='restaurant-detail'),
    path('restorant/<int:restaurant_id>/recipes', views.restorant_spec_recipt.as_view(), name='restaurant-recipe-detail'),
    # recipes starts below
     path('recipes', Recipe_view.as_view(), name='recipe'), 
     path('recipes/<int:pk>', Recipe_detail_view.as_view(), name='restaurant-detail'),
     path('recipes/recipes_ingredient/<int:recipe_id>', recipt_ing_recipt.as_view(), name='recipe-ingredient-detail'),
     path('recipes/recipes_ingredient/', recipt_ing_recipt.as_view(), name='recipe-ingredient'),
    #  path('recipes/<int:Recipe_id>/<int:ingredient_id>', recipt_ing_recipt.as_view(), name='restaurant-detail'),
    #  ingredient starts below
    path('ingredient', Ingredient_view.as_view(), name='ingredient'), 
    path('ingredient/<int:pk>', Ingredient_detail_view.as_view(), name='restaurant-detail'),
    path('ingredient/ingredient_resturant/<int:ingred_id>', ingred_resto_recipt.as_view(), name='ingredient_restorantdetail'),
    path('ingredient/ingredient_resturant/', ingred_resto_recipt.as_view(), name='ingredient_restaurant_detail'),
    

]
