from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status 
from ..models import  Ingredient ,RestaurantIngredient
from ..serializers import  Ingredient_Serializer  , RestaurantIngredient_Serializer
from django.http import  JsonResponse


class Ingredient_view(generics.ListCreateAPIView):
    queryset=Ingredient.objects.all()
    print(queryset)
    serializer_class=Ingredient_Serializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class Ingredient_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ingredient.objects.all()
    serializer_class=Ingredient_Serializer    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
# alfual endezi ayasasbm 

class ingred_resto_recipt(generics.ListCreateAPIView):
    serializer_class = RestaurantIngredient_Serializer
    queryset = RestaurantIngredient.objects.all()
    print('lij mie wana ',queryset)

    def get(self, request, *args, **kwargs):
        ingred_id = self.kwargs.get('ingred_id')
        # print(ingred_id, "yihe demo")
        
            
        ermias = RestaurantIngredient.objects.filter(ingredient=ingred_id)
        # print(ermias,"dkfjakldklfjkdjd jdklsflkdhfjkdbhgkdjlsfhnj fhdxhfjdk vjkjvhdfilgdlighlrkghli jkrh ilgrah")
               
        data=[{  'ing_id':item.ingredient.ing_id ,'Ingredientname': item.ingredient.Ingredientname, 'resto_id':item.Restourant.resto_id, 'resto_name': item.Restourant.resto_name} for item in ermias]
        
        return JsonResponse(data, safe=False)
       

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
