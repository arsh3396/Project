from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name='myapp'

urlpatterns = [
    # url level caching
    # path('', cache_page(60*15)(views.index), name='index'),
    
    #URL patterns of API
    path('items-json', views.item_list_json, name='item_list_json'),
    
    #URL pattern for API built with DRF
    path('items-api/', views.item_list_api, name = "item_list_api"),
    
    # URL pattern for single item
    path('api/items/<int:pk>/', views.item_detail_api, name='item_detail_api'),
    
    
    # URL Patterns of django app
    path('', views.index, name='index'),
    path('item/', views.item),
    path('<int:id>/', views.detail, name='item_detail'),
    path('add/', views.createItem, name='create_item'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update_item'),
    path('delete/<int:pk>/', views.ItemDelete.as_view(), name='delete_item'),
    
]
