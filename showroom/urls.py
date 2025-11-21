from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('customers/', include('customers.urls')),
    path('sales/', include('sales.urls')),
    path('inventory/', include('inventory.urls')),
    path('', views.index, name='index'),
]

# Serve static files in development
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    # Additional static file serving as backup
    if settings.STATICFILES_DIRS:
        urlpatterns += static(settings.STATIC_URL, document_root=str(settings.STATICFILES_DIRS[0]))
