
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alquiler.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += staticfiles_urlpatterns()