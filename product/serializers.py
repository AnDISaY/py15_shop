from rest_framework import serializers
from product.models import Product, Category, Comment

# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField()
#     slug = serializers.SlugField()


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#
#
# class ProductDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'text', 'rating']

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError('Рейтинг должен быть от одного до пяти')
        return rating

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create('validated_data')
