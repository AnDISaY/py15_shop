from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, CategoryViewSet, CommentViewSet

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# path('api/v1/products/', ProductViewSet.as_view(
#     {'get': 'list',
#      'post': 'create',
#      }
# )),
# path('api/v1/products/<int:pk>/', ProductViewSet.as_view(
#     {'get': 'retrieve',
#      'put': 'update',
#      'patch': 'partial_update',
#      'delete': 'destroy'
#      }
