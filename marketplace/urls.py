from django.urls import path

from . import views

app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add-item/', views.add_item, name='add_item'),

]
