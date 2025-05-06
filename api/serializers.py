from rest_framework import serializers
from store.models import Book, Category
from order.models import Order
from store.models import Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ReviewSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'customer', 'review_star', 'review_text', 'created']
        read_only_fields = ['customer', 'created']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    writer = serializers.StringRelatedField(read_only=True)
    reviews = ReviewSerializer(source='review_set', many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'name', 'slug', 'price', 'stock', 'coverpage', 'bookpage',
            'created', 'updated', 'totalreview', 'totalrating', 'status', 'description',
            'category', 'writer', 'reviews'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'created', 'updated', 'paid'] 