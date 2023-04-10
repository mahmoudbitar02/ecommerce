#view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def productlist_api(request):
    products= Product.objects.all()
    data = ProductSerializer(products,many=True).data
    return Response({'data':data})

