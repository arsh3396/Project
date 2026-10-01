from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
app_name='myapp'

router = DefaultRouter()
router.register(r"items", views.ItemViewSet, basename='item')

urlpatterns = [
    path('api/', include(router.urls)),
    # url level caching
    # path('', cache_page(60*15)(views.index), name='index'),

    #URL pattern for API built with DRF
    # path('api/items/', views.ItemListCreateAPI.as_view(), name = "item_list_api"),
    
    # URL pattern for single item
    # path('api/items/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view(), name='item_detail_api'),
    
    
    # URL Patterns of django app
    path('', views.index, name='index'),
    path('item/', views.item),
    path('<int:id>/', views.detail, name='item_detail'),
    path('add/', views.createItem, name='create_item'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update_item'),
    path('delete/<int:pk>/', views.ItemDelete.as_view(), name='delete_item'),
    
]
