import logging

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Product
from .models import Category 
from .serializers import ProductSerializer
from .serializers import CategorySerializer

logger = logging.getLogger(__name__)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by("-id")
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        logger.info("A product is added: id=%s name=%s", product.id, product.name)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
class CategoryViewSet(viewsets.ModelViewSet):   
    queryset = Category.objects.order_by("-id")
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]