from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('products', views.ProductViewSet)
router.register('carts', views.CartViewSet)

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')

#  URLConf
# urlpatterns = router.urls

urlpatterns = [
    # the asview() wil convert methods into normal functions
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.collection_detail,
         name='collection-detail'),
    #                   ^--- id converter
]

urlpatterns += router.urls
urlpatterns += cart_router.urls
