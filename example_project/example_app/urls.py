from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('index', index),
    path('contact', contact),
    path('products', products),
    path('stock', stock),
    path('products_create', products_create),
    path('supplier_create', supplier_create),
    path('stock_add', stock_add),
    path('deal', deal),
    path('login', login_view),
    path('logout',logout_view),
]