from django.urls import include, re_path
from orders import views


urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
]