from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

app_name = 'marketplace'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add-item/', views.add_item, name='add_item'),
    path('search/', views.search, name='search'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user-<int:seller_id>/', views.user, name='user'),
    path('map/', views.map, name='map'),
    path('inbox/', views.inbox, name = 'inbox'),
    path('outbox/', views.outbox, name = 'outbox'),
    url(r'^advFilter/$', views.advFilter, name='advFilter'),
    path('message/', views.message, name = 'message'),
    path('message/<int:user_id>/', views.message, name = 'message'),
    path('reply/<int:message_id>/', views.reply, name = 'reply'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
    path('<int:item_id>/markSold/', views.markSold, name='markSold')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
