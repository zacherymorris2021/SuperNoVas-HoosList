from django.urls import path

from . import views

app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add-item/', views.add_item, name='add_item'),
    path('search/', views.search, name='search'),
    path('user-<int:seller_id>/', views.user, name='user'),
    path('user-<int:seller_id>/rate/', views.rate, name='rate'),
    path('filter/', views.filter, name = 'filter')
]
