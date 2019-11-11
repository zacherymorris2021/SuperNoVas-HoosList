from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add-item/', views.add_item, name='add_item'),
    path('search/', views.search, name='search'),
    path('user-<int:seller_id>/', views.user, name='user'),
    path('user-<int:seller_id>/rate/', views.rate, name='rate'),
    path('map/', views.map, name='map'),
    path('filter/', views.filter, name = 'filter')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)