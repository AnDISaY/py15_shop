from rest_framework import serializers

from order.models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    positions = OrderItemSerializer(write_only=True, many=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['positions', 'created_at', 'id', 'status']
        # {"products": [{"product": 1(id), "quantity": 2}, {"product":5, "quantity": 1}]}

    def create(self, validated_data):
        products = validated_data.pop('positions')
        user = self.context.get('request').user
        order = Order.objects.create(user=user, status='open')
        for prod in products:
            product = prod['product']
            quantity = prod['quantity']
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['positions'] = OrderItemSerializer(instance.items.all(), many=True).data
        return representation

# TODO: Обновление заказа
# TODO: Список заказов пользователя


