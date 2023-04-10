#view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def productlist_api(request):
    products= Product.objects.all()[:100]
    data = ProductSerializer(products,many=True,context={"request": request}).data ###(context = you can see the image url on API page )
    return Response({'data':data})



class ProductListApi(generics.ListAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer