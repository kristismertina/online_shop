from django.urls import include, re_path,path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog import views as v

app_name = 'blog'
app_shop = 'shop'
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(('blog.urls','blog'), namespace='blog')),
    re_path(r'^cart', include(('cart.urls','cart'), namespace='cart')),
    re_path(r'^shop', include(('shop.urls','shop'), namespace='shop')),
    re_path(r'^orders/', include(('orders.urls', 'order'), namespace='orders')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


