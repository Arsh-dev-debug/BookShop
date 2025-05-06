from rest_framework import viewsets, permissions
from store.models import Book, Category
from order.models import Order
from store.models import Review
from .serializers import BookSerializer, CategorySerializer, OrderSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Review submitted successfully!", "review": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        ) 