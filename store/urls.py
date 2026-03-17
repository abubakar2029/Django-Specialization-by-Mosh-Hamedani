from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet)

# URLConf
# urlpatterns = router.urls

urlpatterns = [
    path('collections/', views.CollectionList.as_view()), # the asview() wil convert methods into normal functions
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
    #                   ^--- id converter
]

urlpatterns += router.urls