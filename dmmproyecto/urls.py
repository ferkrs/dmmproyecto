from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from inicio.views import mi_error_404



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('', include('servicios.urls')),
    path('', include('alfabetizacion.urls')),
    path('', include('reportes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = mi_error_404