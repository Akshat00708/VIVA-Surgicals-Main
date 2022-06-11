from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('product', views.product, name='products')
]

urlpatterns += staticfiles_urlpatterns()
