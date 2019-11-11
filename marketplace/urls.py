from django.urls import path, include
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
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)