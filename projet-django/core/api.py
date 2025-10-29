import logging
from rest_framework import viewsets, permissions 
from .models import Product
from .serializers import ProductSerializer

logger = logging.getLogger(__name__)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by("-id")
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        product = serializer.save()

        logger.info("A product is added: id=%s name=%s", product.id, product.name)

