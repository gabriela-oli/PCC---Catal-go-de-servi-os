from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('site/', include('app.urls')),
    path('produto/', include('produto.urls')),
     path('empresa/', include('empresa.urls')),
]
