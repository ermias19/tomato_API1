from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from .models import Restourant , Recipe, Ingredient, RestaurantIngredient, RecipeIngredient
from .serializers import Restourant_Serializer , Recipe_Serializer ,  Ingredient_Serializer , RestaurantIngredient_Serializer , RecipeIngredient_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

class Restourant_view(generics.ListCreateAPIView):
    queryset=Restourant.objects.all()
    # print(queryset)
    serializer_class=Restourant_Serializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # print(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Restorant_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset=Restourant.objects.all()
    serializer_class=Restourant_Serializer    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
class restorant_spec_recipt(generics.ListAPIView):
    serializer_class=Recipe_Serializer
    def get_queryset(self,*args, **kwargs ):
        restaurant_id=self.kwargs.get('restaurant_id')
        # print(restaurant_id)
        queryset=Recipe.objects.filter(Restourant=restaurant_id)
        return queryset
    



# @api_view(['GET', 'POST'])
# def Restourant_view(request):
#     if request.method=='GET':
#         reto=Restourant.objects.all()
#         resto_serializer=Restourant_Serializer(reto, many=True)
#         return JsonResponse({'retro':resto_serializer.data})
#     if request.method=='POST':
#         serializer=Recipe_Serializer(data=request.data)
#         if serializer.isvalid():
#             serializer.save()
       
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


