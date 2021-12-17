from django.urls import path

from .views import CreateOrderView, UsersOrdersList, UpdateOrder

urlpatterns = [
    path('orders/', CreateOrderView.as_view()),
    path('orders/own/', UsersOrdersList.as_view()),
    path('orders/<int:pk>', UpdateOrder.as_view())
]
