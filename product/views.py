from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


class CategoryListAPIView(APIView):
    def get(self, request):
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None

    def get(self, request, id):
        category_detail = self.get_object(id)
        if category_detail:
            serializer = CategorySerializer(category_detail)
            return Response(serializer.data)
        return Response({'error_message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        category_detail = self.get_object(id)
        if category_detail:
            serializer = CategorySerializer(category_detail, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error_message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        category_detail = self.get_object(id)
        if category_detail:
            category_detail.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error_message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


class ProductListAPIView(APIView):
    def get(self, request):
        product_list = Product.objects.all()
        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None

    def get(self, request, id):
        product_detail = self.get_object(id)
        if product_detail:
            serializer = ProductSerializer(product_detail)
            return Response(serializer.data)
        return Response({'error_message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        product_detail = self.get_object(id)
        if product_detail:
            serializer = ProductSerializer(product_detail, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error_message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        product_detail = self.get_object(id)
        if product_detail:
            product_detail.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error_message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


class ReviewListAPIView(APIView):
    def get(self, request):
        review_list = Review.objects.all()
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Review.objects.get(id=id)
        except Review.DoesNotExist:
            return None

    def get(self, request, id):
        review_detail = self.get_object(id)
        if review_detail:
            serializer = ReviewSerializer(review_detail)
            return Response(serializer.data)
        return Response({'error_message': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        review_detail = self.get_object(id)
        if review_detail:
            serializer = ReviewSerializer(review_detail, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error_message': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        review_detail = self.get_object(id)
        if review_detail:
            review_detail.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error_message': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)


class ProductsWithReviewsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        product_data = []
        for product in products:
            reviews = product.reviews.all()
            total_stars = sum(review.stars for review in reviews)
            average_rating = total_stars / len(reviews) if reviews else 0
            product_data.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'average_rating': average_rating,
            })
        return Response(data=product_data)


class CategoriesWithProductCountAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = [{'id': category.id, 'name': category.name, 'product_count': category.products.count()}
                for category in categories]
        return Response(data=data)
