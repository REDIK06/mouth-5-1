from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category_list = Category.objects.all()
        data = CategorySerializer(category_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category_detail = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error_message': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = CategorySerializer(category_detail).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product_list = Product.objects.all()
        data = ProductSerializer(product_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product_detail = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error_message': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = ProductSerializer(product_detail).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review_list = Review.objects.all()
        data = ReviewSerializer(review_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error_message': 'Отзыв не найден'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = ReviewSerializer(review_detail).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def products_with_reviews(request):
    products = Product.objects.all()
    product_data = ProductSerializer(products, many=True).data

    for product in product_data:
        reviews = product['reviews']
        total_stars = sum(review['stars'] for review in reviews)
        if reviews:
            product['average_rating'] = total_stars / len(reviews)
        else:
            product['average_rating'] = 0

    return Response(data=product_data)


@api_view(['GET'])
def categories_with_product_count(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(data=data)
