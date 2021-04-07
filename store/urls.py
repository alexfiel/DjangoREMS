from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)