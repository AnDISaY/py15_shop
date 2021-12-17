# import rest_framework.pagination
# from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
#     ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from product.filter import ProductFilter
from product.models import Product, Category, Comment
from product.permissions import IsAdmin  # , IsAuthor
from product.serializers import ProductSerializer, CategorySerializer, CommentSerializer  # , ProductsListSerializer


# @api_view(['GET'])
# def product_list(request):
#     pass


# class ProductListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)


# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsListSerializer


# class ProductDetailsView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class CreateProductView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class UpdateProductView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class DeleteProductView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductListCreateView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAdmin]
    # pagination_class = rest_framework.pagination.PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['name', 'price']

    # def get_permissions(self):
    #     if self.action == 'comment':
    #         return []
    #     return [IsAdmin]

    # api/v1/products/id/comment
    # api/v1/products/id/comments/
    @action(['GET'], detail=True)
    def comments(self, request, pk):
        product = self.get_object()
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]


# TODO: Пройтись по всем запросам
# TODO: Комментарии к продуктам
# TODO: Пагинация
# TODO: Заказы
# TODO: Тесты
# TODO: git
# TODO: Документация


# class CreateCommentView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class UpdateCommentView(UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthor]
#
#
# class DeleteCommentView(DestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthor | IsAdmin]


class CommentViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create' :
            return [IsAuthenticated]
        return [IsAdmin]
